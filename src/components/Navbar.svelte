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
    window.history.replaceState(null, "", e.currentTarget.getAttribute("href"));
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
    window.history.replaceState(null, "", `/search?query=${searchQuery}`);
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
    window.addEventListener("resize", updateIsDesktop);
  });

  onDestroy(() => {
    window.removeEventListener("resize", updateIsDesktop);
  });
</script>

<nav class="navbar">
  <a class="logo-link" on:click={handleNavClick} href="/home">
    <img src="/images/icon.png" alt="Logo" class="logo" />
    <span class="eventero-text">Eventero</span>
  </a>

  <!-- Hamburger Icon -->
  {#if !isDesktop}
    <div
      class={`hamburger ${isMenuOpen ? "open" : ""}`}
      on:click={toggleMenu}
      aria-label="Toggle menu"
    >
      <div></div>
      <div></div>
      <div></div>
    </div>
  {/if}

  <!-- Desktop Navigation Links -->
  {#if isDesktop}
    <div class="nav-links">
      <a on:click={handleNavClick} href="/news"> News </a>
      <a on:click={handleNavClick} href="/map"> Map </a>
      <a on:click={handleNavClick} href="/calendar"> Your Calendar</a>
      <a on:click={handleNavClick} href="/events"> Upcoming Events</a>
      <a on:click={handleNavClick} href="/resources"> Resources</a>
      <a on:click={handleNavClick} href="/signup">Sign-Up</a>
      <a on:click={handleNavClick} href="/tags"> Tags </a> 


      <!-- Notification Bell Icon -->
      <button
        type="button"
        class="notification-bell"
        on:click={() => alert("Redirect to notifications page!")}
      >
        <img src="bell.svg" alt="Notifications" class="bell-image" />
        {#if notifications > 0}
          <div class="notification-count">{notifications}</div>
        {/if}
      </button>

    <!-- Added Search Bar and Profile Icon Container for easier formatting. -->
    <div class="search-profile-container">

      <!-- Search Bar -->
      <form on:submit={handleSearch} class="search-bar">
        <input
          type="text"
          bind:value={searchQuery}
          placeholder="Search for resources or events..."
        />
        <button type="submit">Search</button>
      </form>
  
      <!-- Added Profile Icon Here. -->
      <a href="/profile" class="profile-icon">
        <img src="/images/profile_icon.png" alt="Profile" class="profile-image" />
      </a>

    </div>

  </div>
  {/if}
</nav>

<!-- Mobile Navigation Menu -->
{#if !isDesktop && isMenuOpen}
  <div class="nav-links right-side" transition:slide={{ duration: 300 }}>
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
      <img src="bell.svg" alt="Notifications" class="bell-image" />
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
  <button
    class="menu-overlay"
    on:click={toggleMenu}
    on:keydown={(e) => e.key === "Enter" && toggleMenu()}
    aria-label="Close menu"
  ></button>
{/if}

<style>
  @import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap");

/* Profile Icon Styles Added Here. */
.profile-icon {
  cursor: pointer;
  background: none;
  border: none;
  padding: 0;
  margin-left: 15px;
}

.profile-image {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  background-color: transparent;
}

/* Container for Search Bar and Profile Icon Added Here. */
.search-profile-container {
  display: flex;
  align-items: center;
  gap: 10px; /* This Adjusts the spacing between search bar and profile icon. */
}

  .notification-bell {
    position: relative;
    cursor: pointer;
    background: none;
    border: none;
    padding: 0;
  }

  .bell-image {
    width: 28px;
    height: 28px;
    object-fit: cover;
    background-color: transparent;
    transition: 0.2s ease;
  }

/* Hover effect */
.bell-image:hover {
    transform: scale(1.1);
    transition: all 0.1s ease;
}

/* Active (click) effect */
.bell-image:active {
    transform: scale(0.9);
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
    font-family: "Roboto", sans-serif;
    font-weight: bold;
    justify-content: space-between;
    background: #efefef;
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

  .nav-links {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  /* Navigation Links */
  .nav-links a {
    font-weight: 500;
    color: #000000;
    text-decoration: none;
    transition:
      color 0.6s ease,
      background-color 0.6s ease;
    padding: 5px;
    border-radius: 4px;
  }

  .nav-links a:hover {
    color: #ffffff;
    background-color: #004d40;
    transition:
      color 0.3s ease,
      background-color 0.3s ease;
  }

  .nav-links a:active {
    background-color: #00796b; 
    transition: background-color 0.1s ease;
  }

  /* Add separation lines between sidebar links */
  .nav-links.right-side a {
    font-family: "Roboto", sans-serif;
    font-weight: 500;
    position: relative;
    padding: 8px 0;
    padding-left: 8px;
    padding-right: 8px;
    text-decoration: none;
    font-size: 1.3em;
  }

  .nav-links.right-side a:not(:last-child):after {
    content: "";
    display: block;
    width: 100%;
    height: 2px;
    background-color: #ccc;
    position: absolute;
    left: 0;
    bottom: 0;
  }

  /* For sidebar links (when in mobile view) */
  .nav-links.right-side a:hover {
    color: #ffffff;
    background-color: #004d40;
  }

  .nav-links.right-side a:active {
    background-color: #00796b;
    transition: background-color 0.1s ease;
  }

  .nav-links.right-side {
    position: fixed;
    top: 57px;
    right: 0;
    width: 80%;
    max-width: 300px;
    height: calc(100vh - 57px);
    flex-direction: column;
    background-color: #efefef;
    padding: 20px;
    z-index: 1000;
    overflow-y: auto;
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
    object-fit: contain;
  }

  .eventero-text {
    font-weight: bold;
    font-size: 1.8rem;
    color: #085e49;
    margin: 0;
    line-height: 1;
    white-space: nowrap;
    transition: text-shadow 0.5s ease;
    vertical-align: middle;
  }

  .eventero-text:hover {
    text-shadow:
      0 0 15px rgba(0, 0, 0, 0.2),
      0 0 15px rgba(0, 0, 0, 0.2);
    transition: text-shadow 0.5s ease;
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
    border: 1px solid #053a2d;
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
    background-color: #053a2d;
  }

  .search-bar button:active {
    background-color: #00796b;
    transition: background-color 0.1s ease;
  }

  /* Mobile Styles */
  @media (max-width: 768px) {

    .navbar {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 1001;
      background: #efefef;
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
      background-color: #efefef;
      padding: 20px;
      z-index: 1000;
      overflow-y: auto;
    }

    .nav-links.right-side {
      right: 0;
      left: auto;
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
