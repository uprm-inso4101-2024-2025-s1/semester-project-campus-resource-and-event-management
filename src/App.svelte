<script>
  import ExamplePage from "./components/ExamplePage.svelte";
  import CalendarPage from "./components/CalendarPage.svelte";
  import HomePage from "./components/HomePage.svelte";
  import LoginPage from "./components/LoginPage.svelte";
  import SignUpPage from "./components/SignUpPage.svelte";      // sign up
  import SignUpStudent from "./components/SignUpStudent.svelte";  // sign up
  import SignUpOrganization from "./components/SignUpOrganization.svelte";  // sign up
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
  {:else if currentPage == '/signup'}       
    <SignUpPage />
  {:else if currentPage == '/signupstudent'}    
    <SignUpStudent />
  {:else if currentPage == '/signuporganization'} 
    <SignUpOrganization />
  {:else}
    <ExamplePage />
  {/if}
</PageWrapper>