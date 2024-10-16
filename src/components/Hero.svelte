<script>
    import img1 from "../assets/img1.png"
    import img2 from "../assets/img2.jpeg"
</script>

<style>
.hero {
    background-color: #0C9D7A;
    padding: 20px;
}

.hero-img2 {
    display: flex;
    justify-content: space-between;
    margin: 0 0 0 0;
}

.hero-img2 img {
    width: 100%;     
    max-width: 1000px; 
    height: auto;   
    border-radius: 20px;
    margin: 35px 0 26px 20px;
    object-fit: cover;
}

.hero-img1 img {
    width: 100%;     
    max-width: 1000px; 
    height: auto;   
    border-radius: 20px;
    margin: 20px 30px 0 0;
    object-fit: cover;
}

.hero-p {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-end;
    text-align: right;
    margin-left: 30px;
    padding: 5px;
    box-sizing: border-box;
}

.hero-p2 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
    text-align: left;
    padding: 5px;
    box-sizing: border-box;
}

.hero p {
    font-family: 'League Spartan', sans-serif;
    font-weight: 700;
    font-size: 35px;
    line-height: 1.5;
    color: #085E49;
    margin: 0;
}

.hero-img2 button {
    margin: 20px 0 0 0;
    padding: 15px;
    font-size: 16px;
    border-radius: 10px;
    background-color: #0C9D7A;
    color: #fff;
    border: 0.5px solid #0C9D7A;
    cursor: pointer;
    border-color: #fff;
}

.hero-img1 button {
    margin: 20px 0 0 0;
    padding: 15px;
    font-size: 16px;
    border-radius: 10px;
    background-color: #0C9D7A;
    color: #fff;
    border: 0.5px solid #0C9D7A;
    cursor: pointer;
    border-color: #fff;
}

.hero-img1,.hero-img2 {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

@media (min-width: 0px) and (max-width: 533px) {
    .hero-img2 {
        display: block;
        margin: 0 auto;
    }
    .hero-img2 img {
        margin: 0;
    }
    .hero-p {
        text-align: left;
    }
    .hero p {   
        font-size: 20px;
    }
    button {
        margin: 15px 0 0 0;
        padding: 10px;
        font-size: 16px;
    }

    .hero-img1 {
        display: block;
        margin: 0 auto;
    }

    .hero-img1 img {
        margin: 0;
    }
}


@media (min-width: 534px) and (max-width: 767px) {
    .hero p {   
        font-size: 20px;
    }
    button {
        margin: 15px 0 0 0;
        padding: 10px;
        font-size: 16px;
    }
}
</style>

<body>
    <div class="hero">
        <div class="hero-img2">
            <div class="img2"><img src = {img2} alt="img2"></div>
            <div class="hero-p">
                <p>Bring Your Campus Events to Life - Create, Manage,and Share with Ease!
                </p>
                <button>CREATE EVENTS</button>
            </div>
        </div>
        <div class="hero-img1">
            <div class="hero-p2">
                <p>Discover, Engage, and Thrive - Join Campus Events
                and Make the most of Your College Experience!
                </p>            
                <button>FIND EVENTS</button>
            </div>
            <div class="img1"><img src={img1} alt=""></div>
        </div>
    </div>
</body>