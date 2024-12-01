<script>
    let selectedFaculty = "";
    let showassociation = false;
    let pickCount = 5; // Initialize the count to 5
    let selectedTags = [];

    // Dictionary for storing tags according to faculty
    const facultyMajors = {
        "ARTS AND SCIENCES": ["COMPARATIVE LITERATURE", "ECONOMICS", "ENGLISH", "HISTORY", "FRENCH LANGUAGE AND LITERATURE", "HISPANIC STUDIES", "PHILOSOPHY", "PHYSICAL EDUCATION - TEACHING", 
        "PHYSICAL EDUCATION - TRAINING AND OFFICIATING", "VISUAL ARTS", "POLITICAL SCIENCE", "PSYCHOLOGY", "SOCIAL SCIENCES", "SOCIOLOGY", "ART THEORY", "BIOLOGY",
        "INDUSTRIAL BIOTECHNOLOGY", "CHEMISTRY", "GEOLOGY", "MATHEMATICS - PURE MATHEMATICS", "MATHEMATICS - COMPUTER SCIENCE", "MATHEMATICS EDUCATION", "NURSING", "PHYSICS", "PHYSICAL SCIENCES"],
        
        "AGRICULTURAL SCIENCES": ["AGRICULTURAL SCIENCES", "AGRONOMY", "AGRICULTURAL ECONOMICS", "FOOD SCIENCE", "HORTICULTURE", "ANIMAL SCIENCE",
        "CROP PROTECTION", "AGRIBUSINESS", "AGRICULTURAL EDUCATION", "AGRICULTURAL EXTENSION", "SOIL SCIENCE", "AGRICULTURAL AND ENVIRONMENTAL SYSTEMS", "PRE-VETERINARY (NON-DEGREE PROGRAM)"],
        
        "BUSINESS ADMINISTRATION": ["ACCOUNTING", "FINANCE", "HUMAN RESOURCES", "MARKETING", "OPERATIONS MANAGER", "MARKETING", "OPERATIONS MANAGEMENT",
        "COMPUTERIZED INFORMATION SYSTEMS", "OFFICE ADMINISTRATION"],
        
        "ENGINEERING": ["CHEMICAL ENGINEERING", "CIVIL ENGINEERING", "COMPUTER ENGINEERING", "COMPUTER SCIENCE AND ENGINEERING", "ELECTRICAL ENGINEERING", "INDUSTRIAL ENGINEERING",
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
    

    // Redirects to the specified href and updates the current URL
    function redirectToPage(href) {
        window.history.replaceState(null, "", href); // Update the browser URL without reloading
        window.dispatchEvent(new Event("popstate")); // Notify the app of the navigation change
    }

    function handleSubmit() {
        if (isSubmitButton) {
            redirectToPage("/profile"); // Redirect to the desired page
        }
    }

    // Handle tag click and track selected tags
    function handleTagClick(tag) {
        if (selectedTags.includes(tag)) {
            selectedTags = selectedTags.filter(t => t !== tag); // Deselect if already selected
            pickCount += 1;
        } else {
                selectedTags = [...selectedTags, tag]; // Add the tag to selectedTags
                pickCount -= 1;
            }
        }

    $: isSubmitButton = selectedTags.length >= 5; // If 5 tags are selected or more, show "Submit"
    
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
        
        .main-container{
            position: relative;
            width: 100%;
            height: 100%;
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
            position: relative; 
            overflow-y: auto; 
        }

        .bottom-box {
            width: 1207px;
            height: 135px;
            background-color: white;
            position: absolute; 
            bottom: -30px; 
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
            padding: 6px 16px 6px 12px; 
            width: 232px; 
            height: 60px; 
            min-width: 64px; 
            background-color: rgb(8, 94, 73);
            color: white;
            margin: 8px; 
            margin-right: 8px; 
            border-radius: 20px;
            border: 2px solid transparent;
            cursor: pointer;
            font-size: 12px; 
            transition: background-color 0.3s;
        }

        .button:hover {
            background-color: black; 
            border-color: white; 
        }
        .button.selected {
            background-color: grey; /* Grey out the button */
            color: white;
        }

        .pick-button {
            background-color: rgb(8, 94, 73);
            width: 996px;
            height: 87px;
            font-size: 32px;
        }
    </style>
</head>

<body>
    <div class="main-container">
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
                    <p class="section-header">Majors</p>
                    <ul>
                        {#each facultyMajors[selectedFaculty] as tag}
                            <button 
                                class="button {selectedTags.includes(tag) ? 'selected' : ''}" 
                                on:click={() => { handleTagClick(tag); showassociation = true; }}>
                                {tag}
                            </button>
                        {/each}
                    </ul>
                {/if}
                {#if showassociation}
                    <p class="section-header">Associations</p>
                    <ul>
                        {#each combinedAssociations as tag}
                            <button 
                                class="button {selectedTags.includes(tag) ? 'selected' : ''}" 
                                on:click={() => handleTagClick(tag)}>
                                {tag}
                            </button>
                        {/each}
                    </ul>
                {/if}
            </div>
            
            <div class="bottom-box">
                <button class="pick-button"
                on:click={() => {
                    if (isSubmitButton) 
                        window.location.href = "/profile";}}
                >
                    
                    {#if isSubmitButton}
                        Submit
                    {:else}
                        Pick {pickCount} or more
                    {/if}
                </button>
            </div>
        </div>
    </div>
</body>
