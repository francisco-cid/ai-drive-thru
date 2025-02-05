<script lang="ts">
    import { Card } from "$lib/components/ui/card";
    import { Input } from "$lib/components/ui/input";
    import { Button } from "$lib/components/ui/button";
    import OrderHistory from "./OrderHistory.svelte";
    import { postOrder, fetchOrders } from "$lib/api";

    // states received as props from +page.ts
    export let orders: Order[];
    export let totalBurgers: number;
    export let totalFries: number;
    export let totalDrinks: number;

    let orderMessage: string = ""; // user input
    let errorMessage: string | null = null; // tracks errors

    // let orders: Order[] = [
    //     { order_num: 1, burgers: 2, fries: 1, drinks: 0, status: "placed" },
    //     { order_num: 2, burgers: 1, fries: 0, drinks: 2, status: "placed" },
    //     { order_num: 3, burgers: 0, fries: 1, drinks: 1, status: "canceled" }, // Should be filtered out
    //     { order_num: 4, burgers: 3, fries: 2, drinks: 1, status: "placed" },
    // ];
    // called after order successfuly placed to refresh history and counts
    async function loadOrders() {
        console.log("LOADORDERS RUNNING");
        try {
            const data = await fetchOrders();
            // TODO check data.success and data.error
            orders = data.orders;
            totalBurgers = data.total_burgers;
            totalFries = data.total_fries;
            totalDrinks = data.total_drinks;
            errorMessage = null;
        } catch (error) {
            console.error("Failed to refresh orders:", error);
            errorMessage = "Failed to load orders. Please try again.";
        }
    }

    // called on submit to place order
    async function submitOrder() {
        console.log("submitOrder being called");
        if (!orderMessage.trim()) return;
        try {
            const response = await postOrder(orderMessage);
            if (response.success) {
                orderMessage = "";
                await loadOrders(); // ✅ Refresh orders after submission
            } else {
                console.error("Order failed:", response.error);
                errorMessage = response.error;
            }
        } catch (error) {
            console.error("API error:", error);
            errorMessage = "Failed to place order. Please try again.";
        }
    }
</script>

<div class="container mx-auto p-6 space-y-6">
    <!-- Row 1: Totals -->
    <div class="grid grid-cols-3 gap-4">
        <Card class="p-6 text-center">
            <p class="text-lg font-semibold">Total # of Burgers</p>
            <p class="text-2xl">{totalBurgers}</p>
        </Card>
        <Card class="p-6 text-center">
            <p class="text-lg font-semibold">Total # of fries</p>
            <p class="text-2xl">{totalFries}</p>
        </Card>
        <Card class="p-6 text-center">
            <p class="text-lg font-semibold">Total # of drinks</p>
            <p class="text-2xl">{totalDrinks}</p>
        </Card>
    </div>

    <!-- Row 2: Order Input Box -->
    <div class="flex gap-4">
        <Input
            bind:value={orderMessage}
            class="flex-1 p-4"
            placeholder="Ex: &quot;I would like 1 burger & fries&quot;"
        />
        <Button class="p-4" on:click={submitOrder}>Run</Button>
    </div>

    <!-- Row 3: Order History -->
    <OrderHistory {orders} />
    <!-- TODO display error message? -->
</div>
