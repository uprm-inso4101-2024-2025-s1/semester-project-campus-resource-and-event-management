<script>
  import App from "../App.svelte";
  import Footer from "../components/Footer.svelte"
  import Hero from "../components/Hero.svelte"
  import Pop from "../components/pop-up.svelte"
  import arrowsImg from '/images/arrows.png'
</script>

<section class="title-section">
  <div class="title-container">
    <h1>Campus Resource and Event Manager</h1>
    <p>Your gateway to campus life.</p>
  </div>
  <img src={arrowsImg} alt="Decorative arrows" class="arrows">
</section>

<div class="mission-vision-container">

  <div class="card">
    <h3>Mission Statement</h3>
    <p>To simplify event and resource management at UPRM, enhancing student engagement and campus connectivity through an intuitive platform.</p>
  </div>

  <div class="card">
    <h3>Vision Statement</h3>
    <p>To become UPRM's go-to hub for discovering events and resources, fostering a more connected and active student community.</p>
  </div>
  
</div>

<div>
  <Hero/>
</div>

<div class="footerWrapper">
  <Footer/>
</div>

<div>
  <!-- aqui se ve el pop-up de los issue 356 a 359 -->
  <!-- <Pop/> -->
</div>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&display=swap');

  .footerWrapper {
      font-family: 'Roboto', sans-serif;
  }

  .title-section {
    background-color:#D9D9D9;
    padding: 60px 0;
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
  }

  .title-container {
    margin-left: 200px;
    max-width: 700px;
  }

  .title-section h1 {
    font-family: 'League Spartan', sans-serif;
    font-size: 64px;
    font-weight: 700;
    line-height: 80px;
    color: #085e49;
    margin-bottom: 10px;
  }

  .title-section p {
    font-family: 'Roboto', sans-serif;
    font-size: 24px;
    font-weight: 700;
    line-height: 80px;
    color:#085E49;
  }

  .arrows {
    position: absolute;
    top: 113px;
    left: 963px;
    width: 300px; 
    height: 300px;
  }

  .mission-vision-container {
    background-color: #D9D9D9;
    display: flex;
    justify-content: space-around;
    padding: 40px 150px;
    gap: 40px;
    position: relative;
  }

  .card {
    background-color:#D9D9D9;
    border: 2px solid #085e49;
    border-radius: 12px; 
    padding: 30px;
    width: 500px;
    height: 225px; 
    text-align: left;
  }

  .card h3 {
    font-family: 'Roboto', sans-serif;
    font-size: 25px;
    font-weight: 700;
    color: #085e49;
    margin-bottom: 10px;
  }

  .card p {
    font-family: 'Roboto', sans-serif;
    font-size: 18px;
    color: #000;
  }

  @media (max-width: 767px) {
    .title-container {
      margin-left: 20px;
    }

    .mission-vision-container {
      flex-direction: column;
      padding: 40px 50px;
      align-items: center;
    }

    .card {
      width: 100%;
      max-width: 500px;
    }
  }

  @media (max-width: 533px) {
    .title-section h1 {
      font-size: 48px;
      line-height: 60px;
    }

    .title-section p {
      font-size: 20px;
    }
  }
</style>