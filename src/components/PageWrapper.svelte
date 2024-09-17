<script>
  import { onMount } from "svelte";
    import Navbar from "./Navbar.svelte";

  function handleNavClick(e) {
    // Since this is a single page application, doing this will prevent
    // uncecessary refreshing of the page every time a nav link is clicked on
    e.preventDefault();
    window.history.replaceState(null, '', e.target.pathname);
  }
  
</script>

<Navbar/>

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