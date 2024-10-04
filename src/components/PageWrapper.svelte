<script>
    import Navbar from "./Navbar.svelte";
    export let currentPage;

</script>

<main>
    <Navbar bind:currentPage />
    <slot />
</main>

<style>
    main {
        flex-direction: column;
        height: 100vh;
        display: flex;
    }
</style>