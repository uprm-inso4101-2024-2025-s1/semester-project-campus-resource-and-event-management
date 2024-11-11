<!-- Temp Map Page -->
<script>
    // import edificios from "../assets/edificio_2.png";
    import edificios from "../assets/mapa-y-edificios.jpg";

    let areas = [
        {
            id: 1,
            label: "1. Taller de Arte en Remodelación",
            left: "43.8%",
            top: "44.7%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 2,
            label: "2. Administración de Empresas [AE]",
            left: "23.2%",
            top: "18.2%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 3,
            label: "3. Almacén del CID",
            left: "83%",
            top: "27.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 4,
            label: "4. Almacén Obras de MuSA",
            left: "60%",
            top: "82.6%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 5,
            label: "5. Antiguo Centro Nuclear (varios programas incluyendo Sea Grant)",
            left: "77.9%",
            top: "26.3%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 6,
            label: "6. Antigua Pista Atlética",
            left: "85.5%",
            top: "87.2%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 7,
            label: "7. Banda y Orquesta",
            left: "80.5%",
            top: "79.6%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 8,
            label: "8. Biblioteca general",
            left: "56.2%",
            top: "61.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 9,
            label: "9. Edificio de Biología [B]",
            left: "63.9%",
            top: "26.3%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 10,
            label: "10. Centro de Cuido Diurno",
            left: "7.5%",
            top: "40.4%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 11,
            label: "11. Centro de Estudiantes",
            left: "64.7%",
            top: "63.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 12,
            label: "12. Central Telefónica",
            left: "43.8%",
            top: "52%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 13,
            label: "13. CISA",
            left: "78.5%",
            top: "21%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 14,
            label: "14. Coliseo Rafael A. Mangual [CM]",
            left: "34.1%",
            top: "61.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 15,
            label: "15. Complejo de Tennis 2010",
            left: "10.9%",
            top: "41.9%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        }
        ];
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

    .hover-area {
        position: absolute;
        background: rgba(255, 0, 0, 0.2);
        /* background: #ff606000; */
        cursor: pointer;
        border-radius: 5px;
    }

    .label {
        position: absolute;
        color: #000;
        background: #ffffff;
        padding: 5px;
        border: 1px solid #000;
        white-space: nowrap;
        z-index: 20;
        border-radius: 5px;
        font-size: 0.9em;
    }
</style>

<body>
    <div class="full-image">
        <img src={edificios} alt="UPRM edificios" />
        <h1 class="title">UPRM edificios</h1>

        {#each areas as area (area.id)}
            <button
                class="hover-area"
                style=
                    "left: {area.left};
                    top: {area.top};
                    width: {area.width};
                    height: {area.height};"
                    on:mouseover={() => area.showLabel = true}
                    on:mouseout={() => area.showLabel = false}
                    on:focus={() => area.showLabel = true}
                    on:blur={() => area.showLabel = false}
                    aria-label="{area.label}"
            ></button>
            {#if area.showLabel}
                <div
                    class="label"
                    style=
                        "left: {area.left};
                        top: calc({area.top} - 30px);"
                >

                    {area.label}
                </div>
            {/if}
        {/each}
    </div>
</body>