<script lang="ts">
    import { Input } from "$lib/components/ui/input";
    import { Button } from "$lib/components/ui/button";
    import { Loader } from "lucide-svelte";

    // receive props
    export let orderMessage: string;
    export let onSubmit: () => Promise<void>;

    let isLoading: boolean = false;

    const handleSubmit = async () => {
        isLoading = true;
        await onSubmit();
        isLoading = false;
    };
</script>

<form on:submit|preventDefault={handleSubmit} class="flex items-center gap-4">
    <Input
        bind:value={orderMessage}
        class="flex-1 p-4 h-20 text-lg"
        placeholder="Ex: &quot;I would like 1 burger & fries&quot;"
        disabled={isLoading}
    />
    <Button
        type="submit"
        class="w-16 h-16 rounded-full text-lg flex items-center justify-center bg-blue-600 hover:bg-blue-700"
        disabled={isLoading}
    >
        {#if isLoading}
            <Loader class="animate-spin" size={24} />
        {:else}
            Run
        {/if}
    </Button>
</form>
