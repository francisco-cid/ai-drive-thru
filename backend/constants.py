LLM_INSTRUCTION_MESSAGES =  [
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "You are an AI assistant that extracts structured order information from user text and returns it in a JSON object. The user may place a new order or cancel an existing one. \nJSON response should contain 3 attributes:\n1. \"action\" : \"order\" or \"cancel\" \n2. \"order_details\": If \"order\" include { \"burgers\": int, \"fries\": int, \"drinks\": int }. If \"cancel\", include {\"order_num\": str}\n3. \"error\": If input is invalid, return an error message here. \n\nOnly recognize \"burgers\", \"fries\", and \"drinks\" as valid menu items. The \"order_num\" is required for cancellations."
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "text": "I'd like 2 burgers and a drink",
                "type": "text"
                }
            ]
            },
            {
            "role": "assistant",
            "content": [
                {
                "text": "{\"action\": \"order\", \"burgers\": 2, \"fries\": 0, \"drinks\": 1, \"error\": null}",
                "type": "text"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "text": "Cancel order 12345",
                "type": "text"
                }
            ]
            },
            {
            "role": "assistant",
            "content": [
                {
                "text": "{\"action\": \"cancel\", \"order_number\": \"12345\", \"error\": null}",
                "type": "text"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "text": "Give me a large steak and salad",
                "type": "text"
                }
            ]
            },
            {
            "role": "assistant",
            "content": [
                {
                "text": "{\"action\": null, \"error\": \"Unable to parse input as a valid order or cancellation. Menu items not identified.\"}",
                "type": "text"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "Give me a coke and a 2 burgers"
                }
            ]
            },
            {
            "role": "assistant",
            "content": [
                {
                "type": "text",
                "text": "{\n  \"action\": \"order\",\n  \"order_details\": {\n    \"burgers\": 2,\n    \"fries\": 0,\n    \"drinks\": 1\n  },\n  \"error\": null\n}"
                }
            ]
            }
        ]

# Define menu items as constants
MENU_ITEMS = {
    "BURGER": "burgers",
    "FRIES": "fries",
    "DRINK": "drinks"
}

# Define possible actions
ACTIONS = {
    "ORDER": "order",
    "CANCEL": "cancel"
}

# Possible status for a saved order
ORDER_STATUS = {
    "PLACED": "placed", 
    "CANCELLED": "canceled"
}