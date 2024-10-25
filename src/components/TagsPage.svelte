
    <script>
    
        let selectedFaculty = "";
        let showassociation = false;

        //dictionary for storing tags according to faculty
       const facultyMajors = {

        "ARTS AND SCIENCES" : ["COMPARATIVE LITERATURE", "ECONOMICS", "ENGLISH", "HISTORY", "FRENCH LANGUAGE AND LITERATURE", "HISPANIC STUDIES", "PHILOSOPHY", "PHYSICAL EDUCATION - TEACHING", 
        "PHYSICAL EDUCATION - TRAINING AND OFFICIATING", "VISUAL ARTS", "POLITICAL SCIENCE", "PSYCHOLOGY", "SOCIAL SCIENCES", "SOCIOLOGY", "ART THEORY", "BIOLOGY",
        "INDUSTRIAL BIOTECHNOLOGY", "CHEMISTRY", "GEOLOGY", "MATHEMATICS - PURE MATHEMATICS", "MATHEMATICS - COMPUTER SCIENCE", "MATHEMATICS EDUCATION", "NURSING", "PHYSICS", "PHYSICAL SCIENCES", ],

        "AGRICULTURAL SCIENCES" : ["AGRICULTURAL SCIENCES", "AGRONOMY", "AGRICULTURAL ECONOMICS", "FOOD SCIENCE", "HORTICULTURE", "ANIMAL SCIENCE",
        "CROP PROTECTION", "AGRIBUSINESS", "AGRICULTURAL EDUCATION", "AGRICULTURAL EXTENSION", "SOIL SCIENCE", "AGRICULTURAL AND ENVIRONMENTAL SYSTEMS", "PRE-VETERINARY (NON-DEGREE PROGRAM)",],

        "BUSINESS ADMINISTRATION" : ["ACCOUNTING", "FINANCE", "HUMAN RESOURCES", "MARKETING", "OPERATIONS MANAGER", "MARKETING", "OPERATIONS MANAGEMENT",
        "COMPUTERIZED INFORMATION SYSTEMS", "OFFICE ADMINISTRATION"],

        "ENGINEERING" : ["CHEMICAL ENGINEERING", "CIVIL ENGINEERING", "COMPUTER ENGINEERING", "COMPUTER SCIENCE AND ENGINEERING", "ELECTRICAL ENGINEERING", "INDUSTRIAL ENGINEERING",
        "MECHANICAL ENGINEERING", "SOFTWARE ENGINEERING", "SURVEYING AND TOPOGRAPHY"]
       };
       const MajorAsociations = {
        "ARTS AND SCIENCES" : ["Orquesta de Cuerdas", "Asociación de estudiantes de Biología", "Asociación de Estudiantes de Ciencias Políticas", "Comite Universitario de Lideres", "Asociación de Estudiantes de Psicología", "Asociación Estudiantil de Biotecnología Industrial", "Asociación de Estudiantes de Historia", 
        "Círculo de Pre-Médicos UPRM"],
        "AGRICULTURAL SCIENCES" : ["Institute of Food Technology Student Association - Puerto RiconChapter", "Asociación Estudiantil de Ciencia Animal", "Asociación de Estudiantes de Agronomía y Suelos", "Asociación de Estudiantes de Protección de Cultivos", "Asociacion Estudiantil de Horticultura", "Círculo de Pre-Veterinaria", "Club 4-H Colegial", "Asociación de Economía Agrícola y Agronegocios",
            "Asociación de Estudiantes de Sistemas Agroambientales"],
        "BUSINESS ADMINISTRATION" : ["Association for Computing Machinery"],
        "ENGINEERING" : ["American Institute of Chemical Engineers", "American Society of Civil Engineers", "American Society for Quality", "Asociacion General de Contratistas",
            "College Robotics for Manufacturing Engineers", " Grupo de Apostolado Católico", "Society of Automotive Engineers", " Circuits and Systems Society", "IEEE Power and Energy Society UPRM",
            "Society of Women Engineers", "Institute of Industrial and Systems Engineers", "IEEE Engineering in Medicine and Biology Society", "IEEE Women in Engineering", "IEEE Eta Kappa Nu", "Institute of electrical and electronics engineers", 
            "IEEE Robotics & Automation Society", "Sociedad de Honor de Ingeniería Industrial Alpha Pi Mu", "American Society of Mechanical Engineers", "Tau Beta Pi", "Asociación de Estudiantes Graduados de Ingeniería Química", "UPRM Moonbuggy Engineering Team",
            "Cru Puerto Rico", "Material Advantage UPRM Chapter", "UPRM Aero Design", "Rotaract Mayaguez Universidad de Puerto Rico", "Human Powered Vehicle Challenge", "Colegio Racing Engineering", "American Society for Engineering Education", "Global Brigades",
            "CAHSI UPRM Student Association", "RUM Racing Baja", "Student Design Competition", "UPRM Roboboat Team", "Cokí Racing Team", "Alpha Astrum"
        ],
       }
        const Universal = {
            "Universal" : ["Fraternidad Alpha Beta Chi Capítulo Beta", "Sororidad Mu Alpha Phi Capítulo Beta","Fraternidad Phi Eta Mu Capítulo Beta", "Fraternidad Nu Sigma Beta", "Coro de Cámara Internacional", "Ride a Bike", "Asociación Estudiantil de Comunicación y Periodismo Científico", "Asociación de Capitanes UPRM", "Asociación Estudiantil de Banda y Orquesta"],
        }

        $: combinedAssociations = [
        ...(MajorAsociations[selectedFaculty] || []),
        ...(Universal.Universal || [])
        ];

    </script>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <title>Centered Box with Inner Content</title>
    
    <style>
        body {
            margin: 0;
            background-color: rgb(12, 123, 96);
            position: relative;
            height: 100vh;
        }

        .outer-box {
            width: 1700px;
            height: 700px;
            background-color: rgb(12, 123, 96, 1); 
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex; 
            justify-content: center; 
            flex-direction: column;
            align-items: center; 
        }

        .inner-box {
            width: 1207px;
            height: 541px;
            background-color: rgb(217,217,217); 
            padding: 20px; 
            border-radius: 20px; 
            text-align: center; 
            color: black;
            font-family: 'Roboto';
            position: relative; /* Added to position child elements absolutely */
            overflow-y: auto; /* Ensures child elements don't overflow */
        }

        .bottom-box{
            width: 1207px;
            height: 135px;
            background-color: white;
            position: absolute; /* Position it absolutely within the inner box */
            bottom: -30px; /* Align it to the bottom */
            left: 130;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 0 0 20px 20px; 
        }
        
        
        h2 {
            margin-top: 12px;
            font-size: 48px;
            font-weight: 500;
        
        }

        p {
            font-size: 24px;
            font-weight: 500;
        }

        .section-header {
            width: 251px;
            height: 44px;
            text-align: left; 
            margin-top: 20px;
            margin-left: 100px; 
            font-size: 24px;
        }

        .button {
            display: inline-block;
            padding: 6px 16px 6px 12px; /* Top, Right, Bottom, Left */
            width: 232px; /* Fixed width */
            height: 60px; /* Fixed height */
            min-width: 64px; /* Minimum width */
            background-color: rgb(8, 94, 73);
            color: white;
            margin: 8px; /* Margin around the button */
            margin-right: 8px; /* To control gap between buttons */
            border-radius: 20px;
            border: 2px solid transparent;
            cursor: pointer;
            font-size: 12px; 
            transition: background-color 0.3s;
        }

        .button:hover {
            background-color: black; /* Change the background color on hover */
            border-color: white; /* Optionally change the border color on hover */
        }

        .pick-button{
            background-color: rgb(8, 94, 73);
            width: 996px;
            height: 87px;
            font-size: 32px;
        }

        
    </style>
    
</head>

<body>
    
    <div class="outer-box">
        <div class="inner-box">
            <h2>What tags would you like to see?</h2>
            <p>These tags will be the tagged events you'll be recommended.</p>
            <p class="section-header">Faculties</p>
            <button class="button" on:click={() => selectedFaculty = "ARTS AND SCIENCES"}>ARTS AND SCIENCES</button>
            <button class="button" on:click={() => selectedFaculty = "AGRICULTURAL SCIENCES"}>AGRICULTURAL SCIENCES</button>
            <button class="button" on:click={() => selectedFaculty = "BUSINESS ADMINISTRATION"}>BUSINESS ADMINISTRATION</button>
            <button class="button" on:click={() => selectedFaculty = "ENGINEERING"}>ENGINEERING</button>

            {#if selectedFaculty}
                <p class = "section-header">Majors</p>
                <ul>
                    {#each facultyMajors[selectedFaculty] as tag}
                        <button class = "button" on:click={() => showassociation = true}>{tag}</button>
                    {/each}
                </ul>
            {/if}
            {#if showassociation}
                <p class="section-header">Associations</p>
                <ul>
                    {#each combinedAssociations as tag}
                    <button class="button">{tag}</button>
                    {/each}
                </ul>
            {/if}

            </div>
        <div class = "bottom-box">
             <button class="button pick-button">Pick 5 or more</button>
        </div>
     </div>
</body>
