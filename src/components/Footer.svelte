<!-- footer -->
<script>
  let facebookLogo = "/images/white-facebook-logo.png";
  let igLogo = "/images/white-insta-logo.png";
  let xLogo = "/images/X_Logo.png";
  let whiteLogo = "/images/eventero-white-logo.png";
  import { onMount } from "svelte";
  let showContacts = false;
  let dialog;
  $: if (dialog && showContacts) {
    dialog.showModal();
    dialog.scrollTo(0, 0);
  }
</script>

<footer>
  <div class="footer-container">
    <dialog
      bind:this={dialog}
      on:close={() => (showContacts = false)}
      on:click|self={() => dialog.close()}
    >
      <div on:click|stopPropagation>
        <slot name="header" class="dialog-content">
          <h3>Postal Address:</h3>
          <p id="footer-address">
            P.O Box 9000 University of Puerto Rico at Mayagüez Calle Post,
            Mayagüez, P.R. 00681-9000
          </p>
          <h3>Fisical Address:</h3>
          <p id="footer-address">
            P.O Box 9000 University of Puerto Rico at Mayagüez Calle Post,
            Mayagüez, P.R. 00681-9000
          </p>
          <h3>Main Telephone: (787) 832-4040</h3>

          <div class="footer-contactUs">
            <div class="footer-contactUs-categorias">
              <h4>Students Services:</h4>
              <div>
                <p>Admissions x2400,X2412</p>
                <p>Dean of Students x3862,3250</p>
                <p>Registrar's Office x3813, x3284</p>
                <p>Clinic, Medical Services x3722 Emergency x2323</p>
                <p>Financial Aid X3863</p>
              </div>
            </div>

            <div class="footer-contactUs-categorias">
              <h4>Faculties:</h4>
              <div>
                <p>College of Business Administration ×3800, x3804</p>
                <p>College of Agricultural Sciences x3850,x1218</p>
                <p>College of Arts & Sciences x3828, x3033</p>
                <p>College of Engineering x3822, x3504</p>
                <p>Dean of Administration x2020, x2024</p>
                <p>Dean of Accademic Affairs x3582, x3807</p>
              </div>
            </div>

            <div class="footer-contactUs-categorias">
              <h4>Investigations:</h4>
              <div>
                <p>Agricultural Extension Service (787) 265-4130, x3592</p>
                <p>Agricultural Experiment Station (787) 833-7765, x3899</p>
                <p>Sea Grant (787) 265-2880, x2165</p>
                <p>Seismic Network (787) 833-8433, x5452</p>
                <p>Center for Economical Development (787) 833-4445, x3613</p>
                <p>
                  Research and Development Center (787) 831-2065, x5250, 5213
                </p>
              </div>
            </div>

            <div class="footer-contactUs-categorias">
              <h4>Other Services:</h4>
              <div>
                <p>Chancellors Office x3131, x3139</p>
                <p>Press and Communications x3879, x2332</p>
                <p>Campus Security x3263, x3872, x2458, x3538</p>
              </div>
            </div>
          </div>
        </slot>
        <button autofocus on:click={() => dialog.close()}>Close</button>
      </div>
    </dialog>
    <div class="footer-page-info">
      <div class="footer-top">
        <h2>Campus Event Life Enhancement</h2>
        <p>
          Discover a vibrant campus experience through our app, designed to
          enhance your involvement in events, activities, and community
          engagement. Our platform fosters a sense of belonging by connecting
          students and staff to events that align with their interests.
        </p>
      </div>

      <div class="footer-bottom">
        <div class="footer-column">
          <h4>Real-Time Resource Availability</h4>
          <p>
            Access real-time updates on the availability of study spaces and
            facilities for convenient booking.
          </p>

          <h4>Streamlined Event Management</h4>
          <p>
            Simplify event organization with tools for creating, promoting, and
            managing events while tracking RSVPs.
          </p>

          <h4>Integrated Navigation Features</h4>
          <p>
            Use integrated maps and navigation tools to easily locate event
            venues and campus resources.
          </p>
        </div>

        <div class="footer-column">
          <h4>Enhanced Communication Channels</h4>
          <p>
            Receive timely updates and announcements from event organizers to be
            up to date and boost participation in campus activities.
          </p>

          <h4>User-Centric Feedback Mechanisms</h4>
          <p>
            Share your feedback through surveys to help us improve the app and
            tailor it to your needs.
          </p>
        </div>
      </div>
    </div>
    <div class="contact-button">
      <button on:click={() => (showContacts = true)}>CONTACT US</button>
    </div>
    <div class="quick-links">
      <div class="footer-column">
        <h5>Quick Links</h5>
        <ul>
          <li><a href="#">Resources</a></li>
          <li><a href="#">Events</a></li>
          <li><a href="#">Map</a></li>
          <li><a href="#">News</a></li>
          <li><a href="#">FAQ</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-termsLegal">
      <a href="https://www.uprm.edu/portales/terminos-y-condiciones-de-uso/">
        <p>Terms of Service and Privacy Policy</p>
      </a>
    </div>
    <div class="footer-rights">
      <a href="https://www.uprm.edu/portales/terminos-y-condiciones-de-uso/">
        <p>©2024 Eventero. All rights reserved.</p>
      </a>
    </div>

    <div class="footer-socialMedia">
      <a
        href="https://www.facebook.com/RecintoUniversitariodeMayaguez/?locale=es_LA"
      >
        <img src={facebookLogo} alt="facebook" class="media-logos" />
      </a>
      <a href="https://www.instagram.com/uprmayaguez/">
        <img src={igLogo} alt="ig" class="media-logos" />
      </a>
      <a href="https://x.com/uprm?lang=es">
        <img src={xLogo} alt="x" class="media-logos" />
      </a>
    </div>
    <img src={whiteLogo} alt="whiteLogo" class="footer-logo" />
  </div>
</footer>

<style>
  dialog {
    width: 100%;
    height: auto;
    max-width: 65rem;
    height: 20rem;
    border-radius: 20px;
    border: none;
    padding: 1.3rem;
    background-color: white;
    top: 30%;
    left: 4rem;
    bottom: 11rem;
    z-index: 10;
    overflow: auto;
    flex-direction: column;
    animation: zoom-in 0.3s ease-out;
    position: absolute;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  }

  dialog button {
    background-color: #17c299;
    color: white;
    outline: none;
  }
  dialog button:hover {
    background: #138e79;
  }
  .dialog-content {
    height: 100%;
    width: 90%;
    position: fixed;
  }
  dialog::backdrop {
    background: transparent;
  }
  dialog > div {
    padding: 1em;
    flex-direction: column;
    justify-content: flex-start;
  }
  dialog::-webkit-scrollbar {
    width: 2em;
    border-radius: 20px;
  }

  dialog::-webkit-scrollbar-track {
    background: transparent;
    border-radius: 100vw;
    margin-block: 0.5em;
  }

  dialog::-webkit-scrollbar-thumb {
    background: #17c299;
    border-radius: 20px;
    border: 0.5em solid white;
  }
  dialog::-webkit-scrollbar-thumb:hover {
    background: #138e79;
  }
  @keyframes zoom-in {
    from {
      transform: scale(0.8);
      opacity: 0;
    }
    to {
      transform: scale(1);
      opacity: 1;
    }
  }

  @keyframes zoom-out {
    from {
      transform: scale(1);
      opacity: 1;
    }
    to {
      transform: scale(0.8);
      opacity: 0;
    }
  }
  @keyframes fade {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  button {
    display: block;
    background-color: #17c299;
    color: white;
    outline: none;
  }

  footer {
    position: relative;
    font-family: "Roboto", sans-serif;
    width: 100%;
    background-color: #053a2d;
    padding: 10rem 0 7rem 0;
    color: white;
    min-height: 400px;
  }
  .footer-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 2rem 0;
  }
  .footer-logo {
    width: 10rem;
    height: auto;
  }
  p,
  h3,
  h4 {
    color: #17c299;
  }
  .contact-button button {
    position: absolute;
    top: 4rem;
    right: 4rem;
    padding: 20px 50px;
    font-size: 1.2rem;
    border: 2px solid #17c299;
    background-color: transparent;
    color: white;
    border-radius: 20px;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    flex: 1;
    outline: none;
  }

  .contact-button button:hover {
    background-color: #17c299;
    color: black;
  }
  .footer-contactUs {
    display: flex;
    width: 100%;
    justify-content: space-around;
  }
  .footer-contactUs-categorias {
    width: 20%;
    height: fit-content;
  }
  a {
    color: #17c299;
    text-decoration: none;
  }
  a:hover {
    color: white;
  }
  h2 {
    margin: 0px 0px 11px 9px;
  }
  h4 {
    font-size: 20px;
    margin: 16px 0px 9px 0px;
  }
  h3 {
    margin: 0 0 -2px 20px;
  }
  #footer-address {
    margin: 0 0 17px 42px;
  }
  p {
    font-size: 20px;
    margin: 0 0 16px 0px;
  }
  .footer-socialMedia {
    width: 100%;
    text-align: center;
  }
  .footer-socialMedia {
    position: absolute;
    bottom: 4rem;
    right: 5rem;
    display: flex;
    justify-content: flex-end;
    gap: 50px;
    align-items: center;
  }
  .footer-socialMedia img {
    width: 1.8rem;
    height: auto;
  }

  .media-logos {
    width: 3rem;
    height: auto;
    max-width: 100%;
  }

  .footer-logo {
    position: absolute;
    bottom: -0.5rem;
    left: 5rem;
    width: 10%;
    height: auto;
  }
  .footer-termsLegal {
    justify-content: center;
    text-align: center;
    position: absolute;
    bottom: 3rem;
    width: 100%;
  }
  .footer-termsLegal a p {
    font-size: 18px;
    color: white;
  }
  .footer-rights {
    justify-content: center;
    text-align: center;
    position: absolute;
    bottom: 2.2rem;
    width: 100%;
  }
  .footer-rights a p {
    font-size: 10px;
    color: white;
  }

  .footer-page-info {
    margin-left: 4rem;
    flex-shrink: 0;
    width: 70%;
  }
  .footer-top {
    flex: 1;
    width: 100%;
    margin-top: -10rem;
  }

  .footer-top h2 {
    margin: 0;
    color: #17c299;
  }
  .footer-top p {
    color: white;
    font-size: large;
  }
  .footer-bottom {
    flex: 1;
    display: flex;
    gap: 3rem;
  }

  .footer-column p {
    color: white;
    font-size: medium;
  }
  .quick-links {
    display: flex;
    gap: 2rem;
    flex: 1;
    margin-left: 8.8rem;
    margin-top: -1.8rem;
  }
  .quick-links li:hover {
    font-weight: bold;
  }
  .footer-column h5 {
    font-size: 20px;
    color: #17c299;
    margin-bottom: 10px;
    font-weight: bold;
  }
  .footer-column {
    flex: unset;
  }

  .footer-column h4 {
    font-size: 16px;
    margin-bottom: 10px;
    font-weight: bold;
  }

  .footer-column ul {
    list-style-type: none;
    padding: 0;
  }

  .footer-column ul li {
    margin-bottom: 10px;
  }

  .footer-column ul li a {
    color: #ffffff;
    text-decoration: none;
  }

  /* mobile */
  @media (min-width: 320px) and (max-width: 767px) and (orientation: portrait) {
    .footer-logo {
      display: none;
    }
    .footer-page-info {
      margin: 0 auto;
      width: 100%;
      padding: 0;
      text-align: center;
    }

    .footer-bottom {
      flex-direction: column;
      align-items: center;
      gap: 0px;
      padding: 0 1rem;
      position: relative;
      top: 30px;
    }

    .footer-column {
      width: 100%;
      text-align: center;
      margin-bottom: 1rem;
    }

    .footer-column p {
      font-size: 1rem;
    }

    .quick-links {
      display: flex;
      flex-direction: column;
      align-items: center;
      position: absolute;
      margin: 0 auto;
      gap: 1rem;
      top: 48rem;
      justify-content: center;
      width: 100%;
      max-width: 1200px;
    }

    .quick-links ul {
      display: flex;
      flex-direction: row;
      justify-content: center;
      gap: 1rem;
    }

    .footer-socialMedia {
      top: 63rem;
      align-self: center;
      right: 7rem;
      margin: 0 auto;
    }

    .footer-logo {
      position: static;
      margin: 7876543rem auto;
      width: 1000%;
    }

    .contact-button {
    display: inline-block; 
    position: absolute; 
    right: 101px; 
    margin: 0 auto;
    top: 54rem; 
    font-weight: bold;
    text-align: center;
}

    .contact-button button {
      align-self: center;
      margin: 0 auto;
      padding: 20px 105px;
      white-space: nowrap;
      justify-content: center;
      position: absolute;
    }

    .footer-socialMedia {
      top: 63rem;
      align-self: center;
      right: 0;
      left: 0;
      margin: 0 auto;
      display: flex;
      justify-content: center;
      gap: 2rem;
      margin-top: 2rem; 
    }

    dialog {
      width: 23.7rem;
      height: 37rem;
      border-radius: 20px;
      border: none;
      padding: 1.3rem;
      background-color: white;
      position: fixed;
      top: 20rem;
      left: 1rem;
      bottom: 11rem;
      z-index: 10;
      overflow: auto;
      flex-direction: column;
      animation: zoom-in 0.3s ease-out;
      position: absolute;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
      overflow-x: hidden;
    }
    .footer-contactUs {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: auto auto;
      gap: 1rem;
      justify-items: start;
      padding: 1rem;
    }

    .footer-contactUs-categorias {
      width: auto;
      margin: 0;
    }
    footer {
      height: 1200px;
    }
  }
</style>
