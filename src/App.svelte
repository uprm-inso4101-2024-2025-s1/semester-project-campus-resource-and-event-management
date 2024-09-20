<script>
  import ExamplePage from "./components/ExamplePage.svelte";
  import CalendarPage from "./components/CalendarPage.svelte";
  import HomePage from "./components/HomePage.svelte";
  import LoginPage from "./components/LoginPage.svelte";
  import PageWrapper from "./components/PageWrapper.svelte";

  let currentPage
</script>

<PageWrapper bind:currentPage>
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