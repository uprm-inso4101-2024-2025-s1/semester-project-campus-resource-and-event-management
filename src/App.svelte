<script>
  import ExamplePage from "./components/ExamplePage.svelte";
  import CalendarPage from "./components/CalendarPage.svelte";
  import HomePage from "./components/HomePage.svelte";
  import LoginPage from "./components/LoginPage.svelte";
  import PageWrapper from "./components/PageWrapper.svelte";

  import { onMount } from "svelte";
  let currentPage = ''

  onMount(() => (currentPage = window.location.pathname))
</script>

<PageWrapper>
  <h2>Current Path: {currentPage}</h2>
  
  {#if currentPage == '/' || currentPage == '/home'}
    <HomePage />
  {:else if currentPage == '/login'}
    <LoginPage />
  {:else if currentPage == '/calendar'}
    <CalendarPage />
  {:else}
    <ExamplePage />
  {/if}
</PageWrapper>