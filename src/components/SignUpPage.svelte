<div class="container">
    <div id="center"> 
        <div id="create"> Create an account </div>
        <div id="createstudent"> 
            <a href="signupstudent" id="studentlink">Create student account</a>
        </div>
        <div id="createorganization"> 
            <a href="signuporganization" id="organizationlink">Create organization account</a>
        </div>
        <div id="already"> Already have an account? </div>
        <div id="login">
            <a href="login" id="loginlink">Log in</a>
        </div>

    </div>
</div>


<style>
    /* ------------  Student CSS ------------ */
    .container {
        display: flex;
        justify-content: center; 
        align-items: center; 
        height: 100vh; 
    }

    #center {
        width: 700px;
        height: 300px;
        border-radius: 10px;
        color: rgb(0,0,0);
        background: rgb(220,220,220);
    }

    #create {
        position: relative;
        top: 35px;
        left: 240px; 
        width: 210px;
        padding: 10px;
        border-radius: 10px;
        font-family: 'Roboto', sans-serif;  
        font-weight: 700; /* Bold */      
        font-size: 23px;
        color: rgb(255,255,255);
        background: rgba(11,93,71,255);
    }

    #createstudent {
        position: relative;
        top: 90px;
        left: 70px;
        width: 235px;
        padding: 10px;
        border-style: solid;
        border-width: 1.5px;
        border-radius: 10px;
        border-color: rgba(11,93,71,255);
        font-family: 'Roboto', sans-serif;  
        font-weight: 700; /* Bold */      
        font-size: 20px;
    }

    #createorganization {
        position: relative;
        top: 37px;
        left: 350px; 
        width: 280px;
        padding: 10px;
        border-style: solid;
        border-width: 1.5px;
        border-radius: 10px;
        border-color: rgba(11,93,71,255);
        font-family: 'Roboto', sans-serif;  
        font-weight: 700; /* Bold */      
        font-size: 20px;
    }

    #studentlink {
        color: rgba(11,93,71,255);
        text-decoration: none;
    }

    #studentlink:hover {
        color: rgba(0,180,80,100);
        text-decoration: none;
    }

    #organizationlink {
        color: rgba(11,93,71,255);
        text-decoration: none;
    }

    #organizationlink:hover {
        color: rgba(0,180,80,100);
        text-decoration: none;
    }

    #already {
        position: relative;
        width: 150px;
        top: 110px;
        left: 245px;
        font-family: 'Roboto', sans-serif;  
        font-weight: 550; /* Bold */    
        font-size: 12px;
        color: rgba(11,93,71,255);

    }

    #login {
        position: relative;
        width: 40px;
        top: 93px;
        left: 390px;
        font-family: 'Roboto', sans-serif;  
        font-weight: 550; /* Bold */ 
        font-size: 12px;
    }

    #loginlink {
        color: rgba(11,93,71,255);
        text-decoration: none;
    }

    #loginlink:hover {
        color: rgba(0,180,80,100);
        text-decoration: none;
    }
    
</style>