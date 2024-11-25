<head>    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  </head>  
  <div class="container">
      <div id="center"> 
          <div id="brand"> EVENTERO </div>    
          <div id="email"> Email </div>
          <input id="emailinput" type="text">
          <div id="psswd"> Password </div>
          <input id="psswdinput" type="password">
          <span class="toggle-password" onclick = "togglePassword()">
              <i class="fas fa-eye"></i>
          </span>
          <div id="showpsswd"> Show Password </div>
          <div id="frgotpsswd"> Forgot Password? </div>
          <div id="loginbutton"> Login </div>
          <div id="instead"> Dont have an account? 
          <a href = "signup" id = "signuplink"> Create an account</a> 
        </div>
      </div>
      <script>
          function togglePassword() {
              const passwordField = document.getElementById('psswdinput');
              const toggleIcon = document.querySelector('.toggle-password i');
  
              if (passwordField.type === 'password') {
                  passwordField.type = 'text';
                  toggleIcon.classList.remove('fa-eye');
                  toggleIcon.classList.add('fa-eye-slash'); // Change to "eye-slash"
              } else {
                  passwordField.type = 'password';
                  toggleIcon.classList.remove('fa-eye-slash');
                  toggleIcon.classList.add('fa-eye'); // Change back to "eye"
              }
          }
      </script>
  </div>
  
  
  
  <style>
      .container {
          display: flex;
          justify-content: center; 
          align-items: center;
          height: 100vh;
      }
  
      #center {
          width: 360px;
          height: 420px;
          border-radius: 10px;
          color: rgb(0,0,0);
          background: rgb(220,220,220);
      }
  
      #brand {
          position: relative;
          top: 30px;
          left: 45px; 
          font-family: 'Roboto', sans-serif;  
          font-weight: 700; /* Bold */      
          font-size: 50px;
          color: rgba(11,93,71,255);
      }

  
      #signuplink {
          color: rgba(11,93,71,255);
          text-decoration: none;
      }
      #email {
          position: relative;
          width: 100px;
          padding: 5px;
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
          padding: 5px;
          top: 45px;
          left: 15px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 550; /* Bold */ 
          font-size: 12px;
          color: rgba(11,93,71,255);
      }
  
      #psswdinput {
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
  
      .toggle-password {
          position: relative;
          top: 77px;
          left: -300px;
      } 
  
      #loginbutton {
          position: relative;
          background: rgba(11,93,71,255);
          width: 310px;
          top: 15px;
          left: 15px;
          padding: 10px;
          border-radius: 10px;
          font-family: 'Roboto', sans-serif;  
          font-weight: 700; /* Bold */ 
          font-size: 18px;
          margin-top: 25px;
          text-align: center;
          color: rgb(255,255,255);
      }
      #showpsswd{
        display: inline-block;
        margin-top: 50px;
        margin-left: 35px;
        font-family: 'Roboto', sans-serif;  
        font-size: 10.5px;
        color: rgba(11,93,71,255);
      }

      #frgotpsswd{
        display: inline-block;
        top: 45px;
        left: 80px;
        margin-top: 25px;
        margin-left: 130px;
        font-family: 'Roboto', sans-serif;  
        font-size: 10.5px;
        color: rgba(11,93,71,255);
      }

      #instead {
          position: relative;
          text-align: center;
          top: 20px;
          left: 5px;
          font-family: 'Roboto', sans-serif;   
          font-size: 12px;
          color: rgba(11,93,71,255);
  
      }
  </style>