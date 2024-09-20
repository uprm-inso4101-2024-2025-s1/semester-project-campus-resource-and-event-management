<script>
    import Navbar from "./Navbar.svelte";
    export let currentPage;

</script>

<Navbar bind:currentPage />

<slot />