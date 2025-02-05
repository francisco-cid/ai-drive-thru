<script lang="ts">
    import { Input } from "$lib/components/ui/input";
    import { Button } from "$lib/components/ui/button";

    // receive props
    export let orderMessage: string;
    export let onSubmit: () => Promise<void>;
</script>

<form on:submit|preventDefault={onSubmit} class="flex items-center gap-4">
    <Input
        bind:value={orderMessage}
        class="flex-1 p-4 h-20 text-lg"
        placeholder="Ex: &quot;I would like 1 burger & fries&quot;"
    />
    <Button
        type="submit"
        class="w-16 h-16 rounded-full text-lg flex items-center justify-center bg-blue-600 hover:bg-blue-700"
        on:click={onSubmit}>Run</Button
    >
</form>
