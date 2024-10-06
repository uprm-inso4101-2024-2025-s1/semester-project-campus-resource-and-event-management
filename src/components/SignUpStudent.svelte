
<script>
    let studentId = '';
    let email = '';
    let password = '';
    let confirmPassword = '';

    async function handleStudentSignup() {
        // Basic password matching validation
        if (password !== confirmPassword) {
            alert('Passwords do not match');
            return;
        }

        const response = await fetch('/signup/student', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                student_id: studentId,
                email: email,
                password: password,
            }),
        });

        const data = await response.json();
        if (response.ok) {
            alert(data.message);  // Show success message
            // Optionally, redirect to another page or clear the form
        } else {
            alert(data.message);  // Show error message
        }
    }
</script>




<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>


<div class="container">
    <div id="center"> 
        <div id="create"> Create a student account </div>
        <div id="already"> Already have an account? </div>
        <div id="login">
            <a href="login" id="loginlink">Log in</a>
        </div>        
        <div id="id"> Student ID </div>
        <input id="idinput" type="text" bind:value={studentId}>
        <div id="email"> Email Address </div>
        <input id="emailinput" type="text" bind:value={email}>
        <div id="psswd"> Password </div>
        <div id="psswdd"> Confirm your password </div>
        <input id="psswdinput" type="password" bind:value={password}>
        <input id="psswddinput" type="password" bind:value={confirmPassword}>
        <span class="toggle-password" onclick="togglePassword()">
            <i class="fas fa-eye"></i>
        </span>
        <div id="characters"> Use 8 or more characters with a mix of letter and symbols </div>
        <div id="showpsswd"> Show password </div>
        <div id="match"> Passwords do not match </div>
        <div id="instead"> Log in instead </div>
          <div id="createbutton"> Create account </div>
        <!-- <div id="createbutton" on:click={handleStudentSignup}> Create account </div> -->

      </div>
      <script>
          function togglePassword() {
              const passwordField = document.getElementById('psswdinput');
              const passwordField2 = document.getElementById('psswddinput');
              const toggleIcon = document.querySelector('.toggle-password i');
  
              if (passwordField.type === 'password') {
                  passwordField.type = 'text';
                  passwordField2.type = 'text';
                  toggleIcon.classList.remove('fa-eye');
                  toggleIcon.classList.add('fa-eye-slash'); // Change to "eye-slash"
              } else {
                  passwordField.type = 'password';
                  passwordField2.type = 'password';
                  toggleIcon.classList.remove('fa-eye-slash');
                  toggleIcon.classList.add('fa-eye'); // Change back to "eye"
              }
          }
  
          const passwordInput = document.getElementById("psswdinput");
          const alertMessage = document.getElementById("characters");
  
          const passwordInput2 = document.getElementById("psswddinput");
          const alertMessage2 = document.getElementById("match");
  
          passwordInput.addEventListener("input", function() {
              let valid = true;
              const value = passwordInput.value;
  
              if (!value.match(/[a-z]/g)) {
                  valid = false;
              }
  
              if (!value.match(/[A-Z]/g)) {
                  valid = false;
              }
  
              if (!value.match(/[0-9]/g)) {
                  valid = false;
              }
  
              if (!value.match(/[\!\@\#\$\%\^\&\*\(\)\_\+\-\=\.\?]/g)) {
                  valid = false;
              }
  
              if (value.length < 8) {
                  valid = false;
              }
  
              if (!valid) {
                  alertMessage.style.color = "red";
              } else {
                  alertMessage.style.color = "green";
              }
          });
  
          passwordInput.addEventListener("input", function() {
              if(passwordInput2.value == passwordInput.value) {
                  alertMessage2.style.display = "none";
              } else {
                  alertMessage2.style.display = "inline";
              }
          });
  
          passwordInput2.addEventListener("input", function() {
              if(passwordInput2.value == passwordInput.value) {
                  alertMessage2.style.display = "none";
              } else {
                  alertMessage2.style.display = "inline";
              }
          });
      </script>
  </div>
  
  
  
  <style>
      .container {
          display: flex;
          justify-content: center; /* this was centered */
      }
  
      #center {
          width: 360px;
          height: 420px;
          border-radius: 10px;
          color: rgb(0,0,0);
          background: rgb(220,220,220);
      }
  
      #create {
          position: relative;
          top: 30px;
          left: 20px; 
          font-family: 'Roboto', sans-serif;  
          font-weight: 700; /* Bold */      
          font-size: 23px;
          color: rgba(11,93,71,255);
      }
  
      #already {
          position: relative;
          width: 150px;
          top: 30px;
          left: 20px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */    
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #login {
          position: relative;
          width: 40px;
          top: 13px;
          left: 175px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #loginlink {
          color: rgba(11,93,71,255);
          text-decoration: none;
      }
  
      #id {
          position: relative;
          width: 60px;
          top: 30px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #idinput {
          position: relative;
          width: 310px;
          padding: 10px;
          border-radius: 10px;
          border-width: 1px;
          background: rgb(220,220,220);
          top: 30px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #email {
          position: relative;
          width: 100px;
          top: 45px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #emailinput {
          position: relative;
          width: 310px;
          padding: 10px;
          border-radius: 10px;
          border-width: 1px;
          background: rgb(220,220,220);
          top: 45px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #psswd {
          position: relative;
          width: 100px;
          top: 60px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #psswdd {
          position: relative;
          width: 150px;
          top: 43px;
          left: 185px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #psswdinput {
          position: relative;
          width: 142px;
          padding: 10px;
          border-radius: 10px;
          border-width: 1px;
          background: rgb(220,220,220);
          top: 45px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #psswddinput{
          position: relative;
          width: 142px;
          padding: 10px;
          border-radius: 10px;
          border-width: 1px;
          background: rgb(220,220,220);
          top: 45px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      .toggle-password {
          position: relative;
          top: 95px;
          left: -320px;
      }
  
      #characters {
          position: relative;
          width: 300px;
          top: 50px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 10.5px;
          color: rgba(11,93,71,255);;
      }
  
      #showpsswd {
          position: relative;
          width: 300px;
          top: 50px;
          left: 40px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 10.5px;
          color: rgba(11,93,71,255);
  
      }
  
      #match {
          position: relative;
          width: 300px;
          top: 35px;
          left: 200px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 10.5px;
          color: rgb(255, 0, 0);
          display: none;
      }
  
      #instead {
          position: relative;
          width: 300px;
          top: 95px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 10px;
          color: rgba(11,93,71,255);
  
      }
  
      #createbutton {
          position: relative;
          background: rgba(11,93,71,255);
          width: 140px;
          top: 50px;
          left: 170px;
          padding: 10px;
          border-radius: 10px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 700; /* Bold */ 
          font-size: 18px;
          color: rgb(255,255,255);
      }
  </style>
   
      