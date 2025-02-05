<script lang="ts">
    import { Card } from "$lib/components/ui/card";
    import { fade, slide } from "svelte/transition";
    // orders prop
    export let orders: Order[] = [];
    // filtered list of orders to be displayed
    $: activeOrders = orders.filter((order) => order.status === "placed");
    // helper function to format item names
    const formatItemLabel = (itemSingular: string, qty: number): string => {
        if (qty === 0) {
            return "";
        }
        const itemPluralized =
            qty > 1
                ? itemSingular === "fry"
                    ? "fries"
                    : `${itemSingular}s`
                : itemSingular;
        return `${qty} ${itemPluralized}`;
    };
    // formats entire items list correctly
    const formatOrderItems = (order: Order): string =>
        [
            formatItemLabel("burger", order.burgers),
            formatItemLabel("fry", order.fries),
            formatItemLabel("drink", order.drinks),
        ]
            .filter((item) => item !== "") // remove empty strings
            .join(", "); // handle comma placement
</script>

<div class="space-y-4">
    <h2 class="text-lg font-semibold">Order History</h2>
    {#if activeOrders.length > 0}
        <div class="grid gap-2">
            {#each activeOrders as order (order.order_num)}
                <div transition:fade={{ duration: 500 }}>
                    <Card
                        class="p-4 flex justify-between items-center border hover:bg-gray-100"
                    >
                        <span class="text-md"> Order #{order.order_num}</span>
                        <span class="text-md text-muted-foreground">
                            {formatOrderItems(order)}
                        </span>
                    </Card>
                </div>
            {/each}
        </div>
    {:else}
        <p class="text-muted-foreground">No active orders.</p>
    {/if}
</div>
