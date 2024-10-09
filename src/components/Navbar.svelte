<script>
  import { onMount, onDestroy } from "svelte";
  import { slide } from "svelte/transition";
  export let currentPage;
  let searchQuery = "";
  let searchResults = [];
  let isMenuOpen = false;
  let notifications = 6;
  let isDesktop = false;

  function handleNavClick(e) {
    e.preventDefault();
    window.history.replaceState(
      null,
      '',
      e.currentTarget.getAttribute('href')
    );
    currentPage = window.location.pathname;
    isMenuOpen = false;
  }

  function handleSearch(e) {
    e.preventDefault();
    if (!searchQuery.trim()) {
      alert("Please enter a search query.");
      return;
    }
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

  function updateIsDesktop() {
    isDesktop = window.innerWidth >= 769;
  }

  onMount(() => {
    currentPage = window.location.pathname;
    updateIsDesktop();
    window.addEventListener('resize', updateIsDesktop);
  });

  onDestroy(() => {
    window.removeEventListener('resize', updateIsDesktop);
  });
</script>

<nav class="navbar">
  <!-- Hamburger Icon -->
  {#if !isDesktop}
    <div class={`hamburger ${isMenuOpen ? 'open' : ''}`} on:click={toggleMenu}>
      <div></div>
      <div></div>
      <div></div>
    </div>
  {/if}

  <!-- /* TODO: Move to the right the hamburger */ -->

  <a class="logo-link" on:click={handleNavClick} href="/home">
    <img src="/images/icon.png" alt="Logo" class="logo" />
    <span class="eventero-text">Eventero</span>
  </a>

  <!-- Desktop Navigation Links -->
  {#if isDesktop}
    <div class="nav-links">
      <a on:click={handleNavClick} href="/news"> News </a>
      <a on:click={handleNavClick} href="/map"> Map </a>
      <a on:click={handleNavClick} href="/calendar"> Your Calendar</a>
      <a on:click={handleNavClick} href="/events"> Upcoming Events</a>
      <a on:click={handleNavClick} href="/resources"> Resources</a>
      <a on:click={handleNavClick} href="/login">Sign-Up</a>

      <!-- Notification Bell Icon -->
      <button
        type="button"
        class="notification-bell"
        on:click={() => alert("Redirect to notifications page!")}
      >
        <img src="/images/bell.png" alt="Notifications" class="bell-image" />
        {#if notifications > 0}
          <div class="notification-count">{notifications}</div>
        {/if}
      </button>

      <!-- Search Bar -->
      <form on:submit={handleSearch} class="search-bar">
        <input
          type="text"
          bind:value={searchQuery}
          placeholder="Search for resources or events..."
        />
        <button type="submit">Search</button>
      </form>
    </div>
  {/if}
</nav>

<!-- Mobile Navigation Menu -->
{#if !isDesktop && isMenuOpen}
  <div class="nav-links" transition:slide={{ duration: 300 }}>
    <a on:click={handleNavClick} href="/news"> News </a>
    <a on:click={handleNavClick} href="/map"> Map </a>
    <a on:click={handleNavClick} href="/calendar"> Your Calendar</a>
    <a on:click={handleNavClick} href="/events"> Upcoming Events</a>
    <a on:click={handleNavClick} href="/resources"> Resources</a>
    <a on:click={handleNavClick} href="/login">Sign-Up</a>

    <!-- Notification Bell Icon -->
    <button
      type="button"
      class="notification-bell"
      on:click={() => alert("Redirect to notifications page!")}
    >
      <img src="/images/bell.png" alt="Notifications" class="bell-image" />
      {#if notifications > 0}
        <div class="notification-count">{notifications}</div>
      {/if}
    </button>

    <!-- Search Bar -->
    <form on:submit={handleSearch} class="search-bar">
      <input
        type="text"
        bind:value={searchQuery}
        placeholder="Search for resources or events..."
      />
      <button type="submit">Search</button>
    </form>
  </div>
  <!-- Menu Overlay -->
  <div class="menu-overlay" on:click={toggleMenu}></div>
{/if}

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

  .notification-bell {
    position: relative;
    cursor: pointer;
    background: none;
    border: none;
    padding: 0;
  }

  .bell-image {
    width: 24px;
    height: 24px;
    object-fit: cover;
    background-color: transparent;
  }

  .notification-count {
    position: absolute;
    top: -8px;
    right: -8px;
    background-color: red;
    border-radius: 50%;
    padding: 2px 6px;
    font-size: 12px;
    font-weight: bold;
    color: white;
  }

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
    flex-shrink: 0;
  }

  .hamburger {
    display: none;
    flex-direction: column;
    cursor: pointer;
    gap: 5px;
    position: relative;
    width: 30px;
    height: 30px;
    z-index: 1001; 
  }

  .hamburger div {
    width: 100%;
    height: 4px;
    background-color: #004d40;
    position: absolute;
    transition: all 0.3s ease;
  }

  .hamburger div:nth-child(1) {
    top: 0;
  }

  .hamburger div:nth-child(2) {
    top: 12px;
  }

  .hamburger div:nth-child(3) {
    top: 24px;
  }

  .hamburger.open div:nth-child(1) {
    top: 12px;
    transform: rotate(45deg);
  }

  .hamburger.open div:nth-child(2) {
    opacity: 0;
  }

  .hamburger.open div:nth-child(3) {
    top: 12px;
    transform: rotate(-45deg);
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

  /* Navigation Links */
  .nav-links {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .nav-links a {
    font-weight: 500;
    color: #000000; /* Black color */
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
    background-color: #004d40; /* Green background */
    color: white; /* White text */
  }

  .search-bar input::placeholder {
    color: #ffffff; /* White placeholder text */
  }

  .search-bar button {
    background-color: #004d40; /* Green background */
    color: white; /* White text */
    border: none;
    padding: 6px 12px;
    cursor: pointer;
    border-radius: 4px;
  }

  .search-bar button:hover {
    background-color: #053A2D;
  }

  /* Mobile Styles */
  @media (max-width: 768px) {
    /* Adjust body padding to account for fixed navbar */
    body {
      padding-top: 57px;
    }

    .navbar {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 1001;
      background: #EFEFEF;
    }

    .hamburger {
      display: flex;
      color: #004d40;
    }

    .nav-links {
      display: flex;
      position: fixed;
      top: 57px; /* Position below navbar */
      left: 0;
      width: 80%;
      max-width: 300px;
      height: calc(100vh - 57px); /* Adjust height */
      flex-direction: column;
      background-color: #EFEFEF;
      padding: 20px;
      z-index: 1000;
      overflow-y: auto;
    }

    .nav-links a {
      margin: 10px 0;
      font-size: 1.2em;
      color: #000000; /* Ensure links are black on mobile */
    }

    .search-bar {
      flex-direction: column;
      gap: 5px;
      width: 100%;
    }

    .search-bar input,
    .search-bar button {
      width: 100%;
    }

    .notification-bell {
      margin-top: 10px;
    }

    /* Menu Overlay */
    .menu-overlay {
      display: block;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 999; /* Just below the navbar */
    }
  }
</style>
