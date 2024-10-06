
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
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
            background-color: white; 
            padding: 20px; 
            border-radius: 5px; 
            text-align: center; 
            color: black;
            font-family: 'Roboto';
        }

        
    </style>
</head>
<body>
    <div class="outer-box">
        <div class="inner-box">
            <h2>What tags would you like to see?</h2>
            <p>These tags will be the tagged events you'll be recommended.</p>
        </div>
    </div>
</body>
</html>
