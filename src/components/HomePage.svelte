
<!-- <footer>
    <p>&copy; 2024 Eventero. All rights reserved.</p>
    <nav>
      <ul>
        <li><a href="#">About Us</a></li>
        <li><a href="#">Contact</a></li>
        <li><a href="#">Terms of Service</a></li>
        <li><a href="#">Privacy Policy</a></li>
      </ul>
    </nav>

    <div class="social-icons">
      <a href="https://www.facebook.com/RecintoUniversitariodeMayaguez" target="_blank">
        <img src="/images/FB_Logo_white.png" alt="Facebook" class="social-icon" />
      </a>
      <a href="https://www.youtube.com/user/videocolegio" target="_blank">
        <img src="/images/YT_Logo_white.png" alt="YouTube" class="social-icon-youtube" />
      </a>
      <a href="https://twitter.com/PrensaRUM" target="_blank">
        <img src="/images/X_Logo.png" alt="X" class="social-icon" />
      </a>
    </div>
  
</footer> -->

<!-- <style>
    footer {
    background-color: #053A2D;
    padding: 20px;
    text-align: center;
  }


  footer nav ul {
    list-style: none;
    display: flex;
    justify-content: space-between;
    font-weight: 500;
    color: #000000;
    text-decoration: inherit;
    margin: 0 10px;
  }

  .social-icon {
    width: 50px;
    height: auto;
    object-fit: contain;
  }
  @media (max-width: 480px) {
    footer nav ul {
        flex-direction: column; /* Stack the footer links vertically */
        text-align: center;
    }
}
.social-icon-youtube {
    width: 80px; 
    height: 40px;  
    background-image: url('/images/YT_Logo_white.png'); 
    background-position: center;  
    background-size: 150%; 
}
  .social-icons a {
    margin: 0 30px;
  }
</style> -->


<script>
  import Footer from "../components/Footer.svelte"
</script>


<section class="title-section">
  <h1>Campus Resource and Event Manager</h1>
  <p>Your gateway to campus life.</p>
</section>


<section class="title-section">
  <h1>Campus Resource and Event Manager</h1>
  <p>Your gateway to campus life.</p>
</section>

<div class="footerWrapper">
  <Footer/>
</div>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
  .footerWrapper {
      font-family: 'Roboto', sans-serif;
  }

  .title-section {
    padding: 40px;
    background-color: #ffffff;
  }

  .title-container {
    margin-left: 200px; /* Adjust based on Figma specs */
    text-align: left;
    max-width: 700px; /* Optional, to constrain the width */
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