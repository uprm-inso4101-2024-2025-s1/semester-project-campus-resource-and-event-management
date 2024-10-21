<!-- Temp Map Page -->
<script>
    import edificios from "../assets/edificio_2.png";
</script>

<style>
    .full-image {
        position: relative;
        width: 100%;
        height: 100vh; 
        overflow: hidden; 
    }

    .title {
        position: absolute; 
        top: 20px; 
        left: 50%; 
        transform: translateX(-50%); 
        color: green; 
        font-size: 3em; 
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); 
        z-index: 10; 
    }

    img {
        width: 100%;
        height: 100%;
        object-fit: cover; 
        border-radius: 20px; 
    }
</style>

<body>
    <div class="full-image">
        <img src={edificios} alt="UPRM edificios" />
        <h1 class="title">UPRM edificios</h1>
    </div>
</body>