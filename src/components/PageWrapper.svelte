<script>
  import { onMount } from "svelte";

  export let currentPage

  function handleNavClick(e) {
    // Since this is a single page application, doing this will prevent
    // uncecessary refreshing of the page every time a nav link is clicked on
    e.preventDefault();
    window.history.replaceState(null, '', e.target.pathname);
    currentPage = window.location.pathname
  }

  onMount(() => (currentPage = window.location.pathname))
</script>

<nav>
  <a on:click={handleNavClick} href="/home">Home</a>
  <a on:click={handleNavClick} href="/login">Login</a>
  <a on:click={handleNavClick} href="/calendar">Calendar</a>
  <a on:click={handleNavClick} href="/example">Example Page With Server Request</a>
</nav>

<slot />

<style>
  nav {
    justify-content: space-around;
    background: #EFEFEF;
    display: flex;
    padding: 2em;
  }

  a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}

  a:hover {
    color: #535bf2;
  }
</style>