<script lang="ts">
    import OrderHistory from "./components/OrderHistory.svelte";
    import OrderForm from "./components/OrderForm.svelte";
    import ItemCounter from "./components/ItemCounter.svelte";
    import ErrorAlert from "$lib/components/custom/ErrorAlert.svelte";
    import { postOrder, fetchOrders } from "$lib/api";

    // props received from load function
    export let data: {
        orders: Order[];
        totalBurgers: number;
        totalFries: number;
        totalDrinks: number;
    };
    let { orders, totalBurgers, totalFries, totalDrinks } = data;

    let orderMessage: string = ""; // user input
    let errorMessage: string | null = null; // tracks errors

    // called after order successfuly placed to refresh history and counts
    async function loadOrders() {
        try {
            const data = await fetchOrders();
            // update states with fresh data
            orders = data.orders;
            totalBurgers = data.total_items_count.burgers;
            totalFries = data.total_items_count.fries;
            totalDrinks = data.total_items_count.drinks;
            errorMessage = null;
        } catch (error) {
            console.error("Failed to refresh orders:", error);
            errorMessage = "Failed to load orders. Please try again.";
        }
    }

    // called on submit to place order
    async function submitOrder() {
        if (!orderMessage.trim()) return;
        try {
            const response = await postOrder(orderMessage);
            // clear user input after success
            orderMessage = "";
            await loadOrders(); // Refresh orders after submission
            errorMessage = "";
        } catch (error) {
            console.error("Error in submitOrder:", error);
            // show only errors coming directly from API logic, everything else gets a generic message
            if (error instanceof Error) {
                errorMessage = error.message.startsWith("API Error")
                    ? error.message // Show our backend/LLM error messages
                    : "Something went wrong. Please try again."; // Generic error for non-API issues
            } else {
                errorMessage = "Something went wrong. Please try again.";
            }
        }
    }
</script>

<!-- Error alert positioned in the top right -->
<ErrorAlert {errorMessage} />
<div class="container mx-auto p-6 space-y-6">
    <!-- Row 1: Totals -->
    <div class="grid grid-cols-3 gap-4">
        <ItemCounter label="Total # of Burgers" count={totalBurgers} />
        <ItemCounter label="Total # of Fries" count={totalFries} />
        <ItemCounter label="Total # of Drinks" count={totalDrinks} />
    </div>

    <!-- Row 2: Order Input Box -->
    <OrderForm bind:orderMessage onSubmit={submitOrder} />

    <!-- Row 3: Order History -->
    <OrderHistory {orders} />
</div>
