<script>
  import Footer from "../components/Footer.svelte"
  import Hero from "../components/Hero.svelte"
</script>

<section class="title-section">
  <h1>Campus Resource and Event Manager</h1>
  <p>Your gateway to campus life.</p>
</section>

<div>
  <Hero/>
</div>

<div class="footerWrapper">
  <Footer/>
</div>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
  .footerWrapper {
      font-family: 'Roboto', sans-serif;
  }

  .title-container {
    margin-left: 200px; 
    text-align: left;
    max-width: 700px; 
  }

  .title-section {
    padding: 40px;
    background-color: #ffffff;
  }

  .title-section h1 {
    font-size: 40px;
    font-weight: 700;
    color: #085E49;
    margin-bottom: 10px;
  }

  .title-section p {
    font-size: 20px;
    color: #004d40;
    margin-top: 5px;
  }
  
</style>