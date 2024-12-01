<script>
  import ExamplePage from "./components/ExamplePage.svelte";
  import CalendarPage from "./components/CalendarPage.svelte";
  import HomePage from "./components/HomePage.svelte";
  import LoginPage from "./components/LoginPage.svelte";
  import PageWrapper from "./components/PageWrapper.svelte";
  import EventsPage from "./components/EventsPage.svelte";
  import MapPage from "./components/MapPage.svelte";
  import NewsPage from "./components/NewsPage.svelte";
  import ResourcesPage from "./components/ResourcesPage.svelte";
  import TagsPage from "./components/TagsPage.svelte";
  import UserProfilePage from "./components/UserProfilePage.svelte";

  let currentPage
</script>

<PageWrapper bind:currentPage>  
  {#if currentPage == '/' || currentPage == '/home'}
    <HomePage />
  {:else if currentPage == '/login'}
    <LoginPage />
  {:else if currentPage == '/calendar'}
    <CalendarPage />
  {:else if currentPage == '/events'}
    <EventsPage />
  {:else if currentPage == '/map'}
    <MapPage />
  {:else if currentPage == '/news'}
    <NewsPage />
  {:else if currentPage == '/resources'}
    <ResourcesPage />
  {:else if currentPage == '/tags'}
    <TagsPage />
  {:else if currentPage == '/profile'}
    <UserProfilePage />
  {:else}
    <ExamplePage />
  {/if}
</PageWrapper>