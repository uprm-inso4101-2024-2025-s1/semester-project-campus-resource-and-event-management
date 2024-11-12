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
        },
        {
            id: 16,
            label: "16. Cuarto Limpio [CID]",
            left: "83.9%",
            top: "30.9%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 17,
            label: "17. Natatorio 2010",
            left: "17.5%",
            top: "35.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 18,
            label: "18. Decanato de Estudiantes (Asistencia Económica/Calidad de Vida/Dept. de Consejería y Servicios Sicológicos)",
            left: "74.6%",
            top: "78%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 19,
            label: "19. Departamento de Edificios y Terrenos",
            left: "33%",
            top: "28%",
            width: '6%',
            height: '15%',
            showLabel: false
        },
        {
            id: 20,
            label: "20. Edificio Sánchez Hidalgo (DECEP/PpMES/Economía) [SH]",
            left: "60.8%",
            top: "46.1%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 21,
            label: "21. Edificio A (Dormitorio de Atletas)",
            left: "6.5%",
            top: "30.1%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 22,
            label: "22. Edificio B (Adm. Pequeños Negocios/Ofic. Adem)",
            left: "10.4%",
            top: "30.1%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 23,
            label: "23. Edificio C (Oficina de Extensión Agrícola)",
            left: "5.1%",
            top: "34.2%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 24,
            label: "24. Edificio D",
            left: "8.1%",
            top: "32%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 25,
            label: "25. Edificio Chardón (Estudios Generales) [CH]",
            left: "71.4%",
            top: "60.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 26,
            label: "26. Edificio Jesús T. Piñero (Ciencias Agrícolas) [P]",
            left: "50.4%",
            top: "82.6%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 27,
            label: "27. Edificio José de Diego",
            left: "69.4%",
            top: "75.1%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 28,
            label: "28. Edificio Luis de Celis (Admisiones-Celis 101/Registro/Decanato de Arte y Ciencias/Estudios Graduados) [C]",
            left: "72.1%",
            top: "66.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 29,
            label: "29. Edificio Luis Monzón [M]",
            left: "64.8%",
            top: "74.3%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 30,
            label: "30. Edificio Luis Stefani [S]",
            left: "77.1%",
            top: "59.2%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 31,
            label: "31. Edificio Oficinas de Facultad",
            left: "56.3%",
            top: "49.7%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 32,
            label: "32. Edificio Ramírez de Arellano y Rosell",
            left: "2.5%",
            top: "43.6%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 33,
            label: "33. Edificio Josefina Torres Torres (Enfermería) [EE]",
            left: "47.8%",
            top: "52%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 34,
            label: "34. Canchas de Racquetball 2010",
            left: "13.3%",
            top: "25.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 35,
            label: "35. Edificio Terrats (Finanzas y Pagaduría) [T]",
            left: "74.5%",
            top: "49.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 36,
            label: "36. Finca Alzamora [AZ]",
            left: "0.5%",
            top: "35.4%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 37,
            label: "37. Física, Geología y Ciencias Marinas [F]",
            left: "71.5%",
            top: "42.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 38,
            label: "38. Gimnasio Ángel F. Espada [GE]",
            left: "43.2%",
            top: "64.6%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 39,
            label: "39. Ofic. en Remodelación Guardia Universitaria",
            left: "73.7%",
            top: "47.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 40,
            label: "40. Imprenta y Artes Plásticas",
            left: "13.6%",
            top: "17.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 41,
            label: "41. Edificio de Ingeniería Civil [CI]",
            left: "50.5%",
            top: "17.4%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 42,
            label: "42. Edificio de Ingeniería Industrial [II]",
            left: "71%",
            top: "50.3%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 43,
            label: "43. Edificio Antonio Luchetti (Ingeniería Mecánica) [L]",
            left: "80.6%",
            top: "70%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 44,
            label: "44. Edificio de Ingeniería Química [IQ]",
            left: "45.9%",
            top: "24.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 45,
            label: "45. Museo de Vehículos Solares",
            left: "75.5%",
            top: "22%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 46,
            label: "46. Laboratorio Ingeniería Agrícola",
            left: "40.3%",
            top: "39%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 47,
            label: "47. Laboratorio de Vehículos Solares",
            left: "76.6%",
            top: "18%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 48,
            label: "48. Centro Interdiciplinario de Estudios del Litoral",
            left: "71.2%",
            top: "22%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 49,
            label: "49. MuSA (Museo y Senado Académico)",
            left: "57.8%",
            top: "76.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 50,
            label: "50. Nueva Pista Atlética",
            left: "27.8%",
            top: "48%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 51,
            label: "51. CID (Oficina Administrativa)",
            left: "79.5%",
            top: "33.3%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 52,
            label: "52. Ofic. Campus Verde (Casa Solar 2005)",
            left: "74%",
            top: "27.3%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 53,
            label: "53. Programa de Rehabilitación Vocacional",
            left: "60.2%",
            top: "38.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 54,
            label: "54. OMCA",
            left: "63.4%",
            top: "40.8%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 55,
            label: "55. Edificio de Química [Q]",
            left: "52.3%",
            top: "42%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 56,
            label: "56. Red Sísmica",
            left: "66%",
            top: "40%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 57,
            label: "57. Residencia del Rector",
            left: "62.6%",
            top: "83.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 58,
            label: "58. R.O.T.C. [SA]",
            left: "79.3%",
            top: "63.5%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 59,
            label: "59. Sendero de los ejercicios",
            left: "23.7%",
            top: "78.2%",
            width: '0.5%',
            height: '0.5%',
            showLabel: false
        },
        {
            id: 60,
            label: "60. Servicios Médicos y Sala de Emergencia",
            left: "57.8%",
            top: "69.7%",
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