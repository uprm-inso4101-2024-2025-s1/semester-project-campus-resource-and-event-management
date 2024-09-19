<script>

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
    }
    .footer-socialMedia h4 {
        margin: 26px 0px 19px 18px;
    }
    .footer-socialMedia-logos {
        display: flex;
        justify-content: center;
        width: 100%;
        gap: 50px; 
    }
    .footer-logo {
        width: 6rem;
        height: auto;
    }

    .footer-termsLegal {
        display: flex;
        width: 100%;
        justify-content: center;
    }
    .footer-termsLegal {
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
     <h2></h2>
    <h3></h3>
    <p id="footer-address"></p>
    <h3></h3>
    <p id="footer-address"></p>
    <h3></h3>

    <div class="footer-contactUs">
        <div class="footer-contactUs-categorias">
            <h4></h4>
            <div>
                <p></p>
                <p></p>
                <p></p>
                <p></p>
                <p></p>
            </div>
        </div>

        <div class="footer-contactUs-categorias">
            <h4></h4>
            <div>
                <p></p>
                <p></p>
                <p></p>
                <p></p>
                <p></p>
                <p></p>
            </div>
        </div>

        <div class="footer-contactUs-categorias">
            <h4>:</h4>
            <div>
                <p></p>
                <p></p>
                <p></p>
                <p></p>
                <p></p>
                <p></p>
            </div>
        </div>

        <div class="footer-contactUs-categorias">
            <h4></h4>
            <div>
                <p></p>
                <p></p>
                <p></p>
            </div>
        </div>
    </div>
        
    <div class="footer-quickLinks">
        <div>
            <h3></h3>
            <p> <a href=""></a></p>
        </div>
        <div>
            <h3></h3>
            <p><a href=""></a></p>
        </div>
        <div>
            <h3></h3>
            <p><a href=""></a></p>
        </div>
        <div>
            <h3></h3>
            <p> <a href=""></a></p>
        </div>
        <div>
            <h3></h3>
            <p><a href=""></a></p>
        </div>
    </div>

    <div class="footer-socialMedia">
        <h4></h4>
        <div class="footer-socialMedia-logos">
            <a href=""><img src = "" alt = "facebook" class="footer-logo footer-logo-facebook"></a> 
            <a href=""><img src = ""alt = "" class="footer-logo footer-logo-facebook"></a>
            <a ><img src = "" class="footer-logo footer-logo-facebook"></a>
        </div>
    </div>
    
     <div class="footer-termsLegal">
        <a href = ""><p  class="footer-terms" ></p></a>
    </div>
</footer>