<script lang="ts">
    import {
        Alert,
        AlertTitle,
        AlertDescription,
    } from "$lib/components/ui/alert";

    // prop
    export let errorMessage: string | null = null;
</script>

{#if errorMessage}
    <div class="fixed top-4 right-4 z-50 w-96">
        <Alert variant="destructive">
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{errorMessage}</AlertDescription>
        </Alert>
    </div>
{/if}
