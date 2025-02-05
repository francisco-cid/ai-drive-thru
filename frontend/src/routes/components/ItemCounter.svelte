<script lang="ts">
    import { Card } from "$lib/components/ui/card";

    export let label: string;
    export let count: number;
</script>

<Card class="p-6 text-center">
    <p class="text-lg font-semibold">{label}</p>
    <p class="text-2xl">{count}</p>
</Card>
