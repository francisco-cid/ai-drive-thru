<script lang="ts">
    import { Card } from "$lib/components/ui/card";
    import { Input } from "$lib/components/ui/input";
    import { Button } from "$lib/components/ui/button";
    import {
        Alert,
        AlertTitle,
        AlertDescription,
    } from "$lib/components/ui/alert";
    import OrderHistory from "./OrderHistory.svelte";
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
{#if errorMessage}
    <div class="fixed top-4 right-4 z-50 w-96">
        <Alert variant="destructive">
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{errorMessage}</AlertDescription>
        </Alert>
    </div>
{/if}
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
    <div class="flex items-center gap-4">
        <Input
            bind:value={orderMessage}
            class="flex-1 p-4 h-20 text-lg"
            placeholder="Ex: &quot;I would like 1 burger & fries&quot;"
        />
        <Button
            class="w-16 h-16 rounded-full text-lg flex items-center justify-center bg-blue-600 hover:bg-blue-700"
            on:click={submitOrder}>Run</Button
        >
    </div>

    <!-- Row 3: Order History -->
    <OrderHistory {orders} />
    <!-- TODO display error message? -->
</div>
