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
            throw new Error(`API Error: ${response.status} ${response.statusText}`);
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
    console.log('customFetch?', customFetch ? 'yes' : 'no')
    const fetchFn = customFetch ?? fetch;
    console.log('fetchFN', fetchFn)
    try {
        const response = await fetchFn(`${BASE_URL}/orders`);
        if (!response.ok) {
            throw new Error(`API Error: ${response.status} ${response.statusText}`);
        }
        return await response.json();
    } catch (err) {
        // TODO improve error logs avoid duplicates
        console.error("Failed to fetch orders:", err);
        throw err;
    }
}