<script>
  import { onMount } from "svelte";
  export let currentPage;
  let searchQuery = "";
  let searchResults = []
  let isMenuOpen = false;

  function handleNavClick(e) {
      e.preventDefault();
      window.history.replaceState(null, '', e.currentTarget.getAttribute('href'));
      currentPage = window.location.pathname;
      isMenuOpen = false;
  }

  function handleSearch(e) {
      e.preventDefault();
      fetchSearchResults(searchQuery);
      window.history.replaceState(null, '', `/search?query=${searchQuery}`);
      currentPage = window.location.pathname;
  }

  // Function to toggle the hamburger menu
  function toggleMenu() {
      isMenuOpen = !isMenuOpen;
  }

  async function fetchSearchResults(query) {
      try {
          const response = await fetch(`/api/search?query=${query}`);
          if (response.ok) {
              searchResults = await response.json(); 
          } else {
              console.error("Search failed", response.statusText);
          }
      } catch (error) {
          console.error("Error fetching search results", error);
      }
  }

  onMount(() => (currentPage = window.location.pathname));
</script>




<nav class="navbar">
  <!-- Hamburger Icon -->
  <div class="hamburger" on:click={toggleMenu}>
      &#9776;
  </div>

  <div class="logo-link">
      <a on:click={handleNavClick} href="/home">
          <img src="/images/icon.png" alt="Logo" class="logo" />
          <span class="eventero-text">Eventero</span> 
      </a>
  </div>

  <div class={`nav-links ${isMenuOpen ? 'open' : ''}`}>
      <a on:click={handleNavClick} href="/news"> News </a>
      <a on:click={handleNavClick} href="/map"> Map </a>
      <a on:click={handleNavClick} href="/calendar"> Your Calendar</a>
      <a on:click={handleNavClick} href="/events"> Upcoming Events</a>
      <a on:click={handleNavClick} href="/resources"> Resources</a>
      <a on:click={handleNavClick} href="/login">Sign-Up</a>

      <!-- Search Bar -->
      <form on:submit={handleSearch} class="search-bar">
          <input type="text" bind:value={searchQuery} placeholder="Search for resources or events..." />
          <button type="submit">Search</button>
      </form>
  </div>
</nav>


<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap'); 

  .navbar {
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
    justify-content: space-between;
    background: #EFEFEF;
    display: flex;
    align-items: center;
    padding: 0 20px;
    height: 57px;
    position: relative;
  }

  .hamburger {
    display: none;
    font-size: 30px;
    cursor: pointer;
  }

  .logo-link {
    display: flex;
    align-items: center;
    text-decoration: none;
    margin-right: auto;
    max-width: 100%;
  }

  .logo {
    max-height: 40px; 
    width: auto;
    margin-right: 10px; 
    object-fit: contain;
  }

  .eventero-text {
    font-weight: bold;
    font-size: 1.8rem; 
    color: #085E49;
    margin: 0;
    line-height: 1; 
    white-space: nowrap; 
    vertical-align: middle;
  }

 /* Hide the Eventero text between 208px and 1045px */
@media (max-width: 1045px) and (min-width: 738px) {
    .eventero-text {
        display: none; /* Hide Eventero text in this range */
    }
}
@media (max-width: 236px) and (min-width: 208px) {
    .eventero-text {
        display: none; /* Hide Eventero text in this range */
    }
}
/* Handling very small windows at 208px width and below */
@media (max-width: 208px) {
    .eventero-text {
        font-size: 1.2rem; /* Reduce text size for smaller screens */
    }

    .logo {
        max-height: 25px; /* Reduce logo size to fit within tiny screen */
    }

    .logo-link {
        justify-content: center; /* Center the logo and text */
    }
}

  .nav-links {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .nav-links a {
    font-weight: 500;
    color: #000000;
    text-decoration: none;
  }

  /* Search Bar Styles */
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

  /* Responsive Styles */
  @media (max-width: 768px) {
    .hamburger {
      display: block;
      color:#004d40
    }

    .nav-links {
      display: none;
      position: absolute;
      top: 57px;
      left: 0;
      width: 100%;
      flex-direction: column;
      background-color: #EFEFEF;
      padding: 20px;
    }

    .nav-links.open {
      display: flex;
    }

    .nav-links a {
      margin: 10px 0;
      font-size: 1.2em;
    }

    .search-bar {
      flex-direction: column;
      gap: 5px;
    }

    .search-bar input {
      width: 100%;
    }

    .search-bar button {
      width: 100%;
    }
  }
</style>