<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <title>Centered Box with Inner Content</title>
    <style>
        body {
            margin: 0;
            background-color: #f4f4f4;
            position: relative;
            height: 100vh;
        }

        .outer-box {
            width: 600px;
            height: 600px;
            background-color: rgb(12, 123, 96); 
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex; 
            justify-content: center; 
            align-items: center; 
        }

        .inner-box {
            width: 500px;
            height: 400px;
            background-color: rgb(217,217,217); 
            padding: 20px; 
            border-radius: 5px; 
            text-align: center; 
            color: black;
            font-family: 'Roboto';
            position: relative; /* Added to position child elements absolutely */
            overflow: hidden; /* Ensures child elements don't overflow */
        }

        .bottom-box{
            width: 500px;
            height: 70px;
            background-color: white;
            position: absolute; /* Position it absolutely within the inner box */
            bottom: 0; /* Align it to the bottom */
            left: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        h2 {
            margin-top: 12px;
            font-size: 22px;
        }

        p {
            font-size: 10px;
            margin-bottom: 20px;
        }

        .faculties {
            text-align: left; 
            margin-left: 20px; 
            font-size: 12px;
        }

        .button {
            display: inline-block;
            padding: 10px 15px;
            background-color: rgb(8, 94, 73);
            color: white;
            margin: 10px;
            margin-right: 10px;
            cursor: pointer;
            font-size: 10px; 
            transition: background-color 0.3s;
        }

        .button:hover {
            background-color: rgb(10, 100, 80);
        }
    </style>
</head>
<body>
    <div class="outer-box">
        <div class="inner-box">
            <h2>What tags would you like to see?</h2>
            <p>These tags will be the tagged events you'll be recommended.</p>
            <p class="faculties">Faculties</p>
            <button class="button">ARTES Y CIENCIAS</button>
            <button class="button">CIENCIAS AGRÍCOLAS</button>
            <button class="button">ADMINISTRACIÓN DE EMPRESAS</button>
            <button class="button">INGENIERÍA</button>
            <div class = "bottom-box">
                <button class="button">Pick 5 or more</button>
            </div>
        </div>
    </div>
</body>
</html>
