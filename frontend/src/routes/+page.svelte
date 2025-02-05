<script lang="ts">
    import { Card } from "$lib/components/ui/card";
    import { Input } from "$lib/components/ui/input";
    import { Button } from "$lib/components/ui/button";
    import OrderHistory from "./OrderHistory.svelte";
    // define types for state variables
    let orderMessage: string = "";
    let totalBurgers: number = 0;
    let totalFries: number = 0;
    let totalDrinks: number = 0;

    // let orders: Order[] = [];
    let orders: Order[] = [
        { order_num: 1, burger: 2, fries: 1, drinks: 0, status: "placed" },
        { order_num: 2, burger: 1, fries: 0, drinks: 2, status: "placed" },
        { order_num: 3, burger: 0, fries: 1, drinks: 1, status: "canceled" }, // Should be filtered out
        { order_num: 4, burger: 3, fries: 2, drinks: 1, status: "placed" },
    ];
    function submitOrder() {
        console.log("order submitted");
        orderMessage = ""; // clear input after submission
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
</div>
