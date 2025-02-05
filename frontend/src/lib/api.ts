const BASE_URL = "http://127.0.0.1:8000"

// calls backend service with user input to place a new order
export async function postOrder(userInput: string) {
    try {
        const response = await fetch(`${BASE_URL}/order`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_txt: userInput }),
        });
        if (!response.ok) {
            throw new Error(`Fetch Error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (err) {
        console.error("Failed to place order:", err);
        throw err // rethrow so caller can handle it
    }
}

// calls backend service to fetch previous orders
// called from both client side component and +page.ts load function
export async function fetchOrders(customFetch?: typeof fetch) {
    // use provided fetch if available (when called from server), otherwise use window.fetch
    const fetchFn = customFetch ?? fetch;
    try {
        const response = await fetchFn(`${BASE_URL}/orders`);
        if (!response.ok) {
            throw new Error(`Fetch Error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (err) {
        throw err;
    }
}