<script>
    import { onMount } from "svelte";
    export let currentPage;

    function handleNavClick(e) {
      // Since this is a single page application, doing this will prevent
      // unnecessary refreshing of the page every time a nav link is clicked on
      e.preventDefault(); 
      window.history.replaceState(null, '', e.currentTarget.getAttribute('href'));
      currentPage = window.location.pathname;
    }

    onMount(() => (currentPage = window.location.pathname))

</script>

<nav>
    <a on:click={handleNavClick} href="/home" class="logo-link">
      <img src="/images/icon.png" alt="Logo" class="logo" />
      <span class="eventero-text">Eventero</span> 
    </a>
    
    <a on:click={handleNavClick} href="/news"> News </a>
    <a on:click={handleNavClick} href="/map"> Map </a>
    <a on:click={handleNavClick} href="/calendar"> Your Calendar</a>
    <a on:click={handleNavClick} href="/events"> Upcoming Events</a>
    <a on:click={handleNavClick} href="/resources"> Resources</a>
    <a on:click={handleNavClick} href="/login">Sign-Up</a>
</nav>





<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');    
    nav {
      font-family: 'Roboto', sans-serif;
      font-weight: bold;
      justify-content: space-around;
      background: #EFEFEF;
      display: flex;
      align-items: center; 
      padding: 0; 
      height: 57px;
    }
  
    a {
    font-weight: 500;
    color: #000000;
    text-decoration: inherit;
    margin: 0 10px;
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
    color: #085E49;
    ; 
    margin-top: -5px;
  }

  .logo-link:hover .eventero-text {
    color: #053A2D;
    ; 
  }
  </style>