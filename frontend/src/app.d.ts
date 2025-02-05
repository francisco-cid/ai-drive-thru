// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}
	// ✅ Global interface for orders (used in API and UI)
	export interface Order {
		order_num: number;
		burger: number;
		fries: number;
		drinks: number;
		status: "placed" | "canceled"; // ✅ Tracks whether the order is active or canceled
	}
}

export { };
