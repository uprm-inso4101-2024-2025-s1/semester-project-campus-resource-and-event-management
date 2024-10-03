<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  </head>
  
  <div class="container2">
      <div id="center2"> 
          <div id="create2"> Create an organization account </div>
          <div id="already2"> Already have an account? </div>
          <div id="login2">
              <a href="login" id="loginlink">Log in</a>
          </div>        
          <div id="name"> Organization name </div>
          <input id="nameinput" type="text">
          <div id="email2"> Email Address </div>
          <input id="emailinput2" type="text">
          <div id="psswd2"> Password </div>
          <div id="psswdd2"> Confirm your password </div>
          <input id="psswdinput2" type="password">
          <input id="psswddinput2" type="password">
          <span class="toggle-password" onclick="togglePassword()">
              <i class="fas fa-eye"></i>
          </span>
          <div id="characters2"> Use 8 or more characters with a mix of letter and symbols </div>
          <div id="showpsswd2"> Show password </div>
          <div id="match2"> Passwords do not match </div>
          <div id="instead2"> Log in instead </div>
          <div id="createbutton2"> Create account </div>
      </div>
      <script>
          function togglePassword() {
              const passwordField = document.getElementById('psswdinput2');
              const passwordField2 = document.getElementById('psswddinput2');
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
  
          const passwordInput = document.getElementById("psswdinput2");
          const alertMessage = document.getElementById("characters2");
  
          const passwordInput2 = document.getElementById("psswddinput2");
          const alertMessage2 = document.getElementById("match2");
  
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
      .container2 {
          display: flex;
          justify-content: center; /* this was centered */
      }
  
      #center2 {
          width: 380px;
          height: 420px;
          border-radius: 10px;
          color: rgb(0,0,0);
          background: rgb(220,220,220);
      }
  
      #create2 {
          position: relative;
          top: 30px;
          left: 20px; 
          font-family: 'Roboto', sans-serif;  
          font-weight: 700; /* Bold */      
          font-size: 23px;
          color: rgba(11,93,71,255);
      }
  
      #already2 {
          position: relative;
          width: 150px;
          top: 30px;
          left: 20px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */    
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #login2 {
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
  
      #name {
          position: relative;
          width: 115px;
          top: 30px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #nameinput {
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
  
      #email2 {
          position: relative;
          width: 100px;
          top: 45px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #emailinput2 {
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
  
      #psswd2 {
          position: relative;
          width: 100px;
          top: 60px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #psswdd2 {
          position: relative;
          width: 150px;
          top: 43px;
          left: 185px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #psswdinput2 {
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
  
      #psswddinput2{
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
  
      #characters2 {
          position: relative;
          width: 300px;
          top: 50px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 10.5px;
          color: rgba(11,93,71,255);
      }
  
      #showpsswd2 {
          position: relative;
          width: 300px;
          top: 50px;
          left: 40px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 10.5px;
          color: rgba(11,93,71,255);
      }
  
      #match2 {
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
  
      #instead2 {
          position: relative;
          width: 300px;
          top: 95px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 10px;
          color: rgba(11,93,71,255);
      }
  
      #createbutton2 {
          position: relative;
          background: rgba(11,93,71,255);
          width: 140px;
          top: 50px;
          left: 190px;
          padding: 10px;
          border-radius: 10px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 700; /* Bold */ 
          font-size: 18px;
          color: rgb(255,255,255);
      }
  </style>