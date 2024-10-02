<!-- footer -->
<script>
    let facebookLogo = "/images/white-facebook-logo.png";
    let igLogo = "/images/white-insta-logo.png";
    let xLogo = "/images/X_Logo.png";
</script>


<style>
    footer {
        width: 100%;
        height: max-content;
        background-color: #0C9D7A;
        margin-top: 1rem;
        padding: 2.5rem 0;
        border-radius: 6px;
        box-shadow: 0px 2px 15px 2px white;
    }
    .footer-logo {
        width: 10rem;
        height: auto;
    }
    p,h2,h3,h4 {
        color: #000000;
    }
    .footer-contactUs {
        display: flex;
        width: 100%;
        justify-content: space-around;
    }
    .footer-contactUs-categorias {
        /* border-radius: 1rem 1rem 1rem 1rem;
        border-color: black;
        border-style: solid; */
        /* box-sizing: border-box; */
        width: 20%;
        height: fit-content;
    }
    a {
        color: blue;
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
    /* .footer-address-h3 {
        margin: 40px 0px 9px 20px;
    } */
    .footer-socialMedia {
        width: 100%;
        text-align: center;
    }
    .footer-socialMedia h4 {
        margin: 0 0 20px 0; 
        font-size: 20px; 
    }
    .footer-socialMedia-logos {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        gap: 50px; 
    }
    .footer-logo {
        width: 4rem;
        height: auto;
    }

    .footer-termsLegal {
        display: flex;
        width: 100%;
        justify-content: center;
        margin: 20px 0 0 0;
        text-align: center;
        align-items: center;
    }
        
    .footer-termsLegal a p {
        font-size: 25px;
    }
    .footer-quickLinks {
        display: flex;
        width: 100%;
        justify-content: space-around;
    }
    .footer-quickLinks div h3 {
        margin: 10px 0px 10px -18px;
    }
    .footer-addres {
        width: 100%;
    }


    /* mobile */
    @media (min-width: 320px) and (max-width: 767px) and (orientation: portrait) {
        .footer-contactUs {
            display: block;
            width: 100%;
        }
        .footer-contactUs-categorias {
            width: 100%;
        }
        .footer-contactUs-categorias h4 {
            margin: 17px 0px 10px 4px;
        }
        h3,p {
            margin: 0 0 0px 10px;
        }
        .footer-socialMedia-logos {
            justify-content: center;      
        }
        .footer-logo {
            width: 4rem;
            height: auto;
        }   

        p {
            margin: 0 0 11px 10px;
        }

        h2 {
            margin: 0px 0px 9px 3px;
        }
        h3 {
            font-size: 23px;
            margin: 0 0 0 5px;
        }
        h4 {
            font-size: 23px;
        }
        .footer-termsLegal a p {
            font-size: 23px;
        }
        .footer-quickLinks {
            display: block;
        }
        .footer-quickLinks div h3 {
            margin: 0 0 0 5px;
        }
        .footer-logo {
            width: 9vh;
        }
        .footer-socialMedia h4 {
            margin: 26px 0px 19px 10px;
        }
    }

</style>

<footer>
    <h2>Contact Us</h2>
    <h3>Postal Address:</h3>
    <p id="footer-address">P.O Box 9000 University of Puerto Rico at Mayagüez Calle Post, Mayagüez, P.R. 00681-9000</p>
    <h3>Fisical Address:</h3>
    <p id="footer-address">P.O Box 9000 University of Puerto Rico at Mayagüez Calle Post, Mayagüez, P.R. 00681-9000</p>
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
                <p>Research and Development Center (787) 831-2065, x5250, 5213</p>
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
        
    <div class="footer-quickLinks">
        <div>
            <h3>Resources:</h3>
            <p>Link <a href="https://www.uprm.edu/area-e/resources/">here</a></p>
        </div>
        <div>
            <h3>Events:</h3>
            <p>Link <a href="https://www.uprm.edu/portada/">here</a></p>
        </div>
        <div>
            <h3>Map:</h3>
            <p>Link <a href="https://uprm.edu/portales/mapa/">here</a></p>
        </div>
        <div>
            <h3>News:</h3>
            <p>Link <a href="https://www.uprm.edu/portada/noticias/">here</a></p>
        </div>
        <div>
            <h3>FAQ:</h3>
            <p>Link <a href="https://www.uprm.edu/placement/inicio/faq/">here</a></p>
        </div>
    </div>

    <div class="footer-socialMedia">
        <h4>Social Media:</h4>
        <div class="footer-socialMedia-logos">
            <a href="https://www.facebook.com/RecintoUniversitariodeMayaguez/?locale=es_LA"><img src={facebookLogo} alt = "facebook" class="footer-logo footer-logo-facebook"></a> 
            <a href="https://www.instagram.com/uprmayaguez/"><img src={igLogo} alt = "ig" class="footer-logo footer-logo-facebook"></a>
            <a href="https://x.com/uprm?lang=es"><img src={xLogo} alt = "x" class="footer-logo footer-logo-facebook"></a>
        </div>
    </div>
    
     <div class="footer-termsLegal">
        <a href="https://www.uprm.edu/portales/terminos-y-condiciones-de-uso/"><p  class="footer-terms" >Terms of Service  and Privacy Policy</p></a>
    </div>
</footer>