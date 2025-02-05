<script lang="ts">
    import { Card } from "$lib/components/ui/card";

    export let label: string;
    export let count: number;
    export let Icon: any;
</script>

<Card
    class="p-6 text-center shadow-md bg-white border border-gray-300 rounded-lg flex flex-col items-center"
>
    <Icon size={32} class="mb-2 text-gray-700" />
    <p class="text-lg font-semibold">{label}</p>
    <p class="text-2xl">{count}</p>
</Card>
