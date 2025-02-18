from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai_client import query_openai
from constants import MENU_ITEMS, ACTIONS, ORDER_STATUS
from fastapi.middleware.cors import CORSMiddleware

# request structure for placing/cancelling order
class OrderRequest(BaseModel):
    user_txt: str

app = FastAPI()

# configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
# in-memory dictionary to store placed orders
orders_db = {}
# tracks total number of menu items ordered
total_items_count = {item: 0 for item in MENU_ITEMS.values()}
# tracks the next available order number
order_counter = 1

# handles order creation and updates item counts
def create_order(order_details):
    global order_counter
     # assign new order number
    order_num = str(order_counter)
    order_counter += 1
    # get count of menu items in order
    order_items_count = {item: order_details.get(item, 0) for item in MENU_ITEMS.values()}
    # save new order
    orders_db[order_num] = { "status": ORDER_STATUS["PLACED"], "items": order_items_count}
    # increase total counts
    for item in MENU_ITEMS.values():
        total_items_count[item] += order_items_count[item]
    return {"success": True, "message": "Order placed successfully", "order_num": order_num, "order_details": orders_db[order_num]}


def cancel_order(order_num):
    if order_num in orders_db:
        # check if already cancelled
        if orders_db[order_num]["status"] == ORDER_STATUS["CANCELLED"]:
            # success with message
            return {"success": True, "message": f"Order {order_num} was already canceled."}
        # decrease total counts to reflect cancellation
        for item in MENU_ITEMS.values():
            total_items_count[item] -= orders_db[order_num]["items"][item]
        # mark order as cancelled
        orders_db[order_num]["status"] = ORDER_STATUS["CANCELLED"]
        return {"success": True, "message": f"Order {order_num} canceled successfully"}
    # Order not found → Raise 404
    raise HTTPException(status_code=404, detail=f"Order {order_num} not found")
        

# translates user input as a valid action and returns fulfilled order or cancellation
@app.post("/order")
async def order(request: OrderRequest):
    # get strucutered ordered information from LLM
    llm_resp = query_openai(request.user_txt)
    # check for errors returned by LLM
    if "error" in llm_resp and llm_resp["error"]:
        raise HTTPException(status_code=400, detail=f"LLM - {llm_resp['error']}")
    
    user_action = llm_resp.get("action")
    order_details = llm_resp.get("order_details", {})

    if user_action == ACTIONS["ORDER"]:
       return create_order(order_details)
    if user_action == ACTIONS["CANCEL"]:
        order_num = order_details.get("order_num")
        return cancel_order(order_num)
    # handle case where LLM returns no error and no valid user action
    raise HTTPException(status_code=400, detail="Invalid action received from LLM")

# returns all placed orders and current counts of ordered menu items
@app.get("/orders")
async def get_orders():
    # convert orders dictionary to list
    orders_list = [{"order_num": order_num, "status": order_data["status"], **order_data["items"]} for order_num, order_data in orders_db.items()]
    return {"success": True, "orders": orders_list, "total_items_count": total_items_count }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
