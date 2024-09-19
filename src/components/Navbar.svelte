<script>
    import { onMount } from "svelte";
    export let currentPage;

    let searchQuery = "";

    function handleNavClick(e) {
      e.preventDefault(); 
      window.history.replaceState(null, '', e.currentTarget.getAttribute('href'));
      currentPage = window.location.pathname;
    }

    onMount(() => (currentPage = window.location.pathname))

    function handleSearch(e) {
  e.preventDefault();
  // Assuming there's a page to handle search results
  window.history.replaceState(null, '', `/search?query=${searchQuery}`);
  currentPage = window.location.pathname;
}


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

    <!-- Search Bar -->
    <form on:submit={handleSearch} class="search-bar">
      <input type="text" bind:value={searchQuery} placeholder="Resources or events..." />
      <button type="submit">Search</button>
  </form>

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
  .search-bar {
  display: flex;
  align-items: center;
  gap: 10px;
}

.search-bar input {
  padding: 6px;
  border: 1px solid #053A2D; 
  border-radius: 4px;
  background-color: #004d40; 
  color: white; 
}

.search-bar input::placeholder {
  color: #ffffff; 
}

.search-bar button {
  background-color: #004d40; 
  color: white;
  border: none;
  padding: 6px 12px;
  cursor: pointer;
  border-radius: 4px;
}

.search-bar button:hover {
  background-color: #053A2D; 
}

  </style>