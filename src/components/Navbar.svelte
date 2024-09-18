<script>
    import { onMount } from "svelte";
    import Navbar from "./Navbar.svelte";

    function handleNavClick(e) {
      // Since this is a single page application, doing this will prevent
      // unnecessary refreshing of the page every time a nav link is clicked on
      e.preventDefault(); 
      window.history.replaceState(null, '', e.currentTarget.getAttribute('href'));
    }

</script>

<nav>
    <a on:click={handleNavClick} href="/home" class="logo-link">
      <img src="/images/1.png" alt="Logo" class="logo" />
      <span class="eventero-text">Eventero</span> 
    </a>
    <a on:click={handleNavClick} href="/login">Login</a>
    <a on:click={handleNavClick} href="/calendar">Calendar</a>
    <a on:click={handleNavClick} href="/example">Example Page With Server Request</a>
</nav>





<style>
    nav {
      justify-content: space-around;
      background: #EFEFEF;
      display: flex;
      align-items: center; 
      padding: 0; 
      height: 57px;
    }
  
    a {
    font-weight: 500;
    color: #646cff;
    text-decoration: inherit;
    margin: 0 10px;
  }
  
    a:hover {
      color: #535bf2;
    }

    .logo-link {
    display: flex;
    align-items: center;
    gap: 0px; 
    text-decoration: none; 
    margin-right: auto ;
  }

  .logo {
    height: 60px; 
    width: auto;
    margin-right: 0px;
  }

  .eventero-text {
    font-weight: bold;
    font-size: 2.0em; 
    color: #006b3f; 
    margin-top: -5px;
  }

  .logo-link:hover .eventero-text {
    color: #004d2f; 
  }
  </style>