// exports load function to handle loading of initial data
// by default runs on server on first load
import { fetchOrders } from "$lib/api";
import type { PageLoad } from "./$types";

export const load: PageLoad = async ({ fetch }) => {
    console.log("Load function... Running on:", import.meta.env.SSR ? "Server" : "Client");
    try {
        const response = await fetchOrders(fetch);
        return {
            orders: response.orders,
            totalBurgers: response.total_items_count.burgers,
            totalFries: response.total_items_count.fries,
            totalDrinks: response.total_items_count.drinks,
        }
    } catch (error) {
        console.error("Failed to fetch initial orders:", error)
        return { orders: [], totalBurgers: 0, totalFries: 0, totalDrinks: 0 }
    }
}