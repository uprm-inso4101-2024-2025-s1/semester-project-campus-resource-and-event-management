<div class="wrapper">
    <button class="addEventButton" on:click={addEvent}>+ Add Event</button>
    
    <div class="color-circle my-events-circle" style="background-color: {isEventBoxActive ? 'green' : 'grey'};"></div>
    <button class="myEventsButton" on:click={myEventsBox}>My Events</button>

    <div class="color-circle other-circle" style="background-color: {isOtherBoxActive ? 'green' : 'grey'};"></div>
    <button class="otherButton" on:click={otherBox}>Other</button>
    <button class="calendarTextBlock">Calendar</button>
    
    <div class="color-circle my-events-circle2" style="background-color: {isEventBoxActive ? 'green' : 'grey'};"></div>
    <button class="addEventButton2" on:click={addEvent}> Select Event</button>

   

</div>

<style>
    .addEventButton2 {
        top:300px;
        cursor: pointer;
    }
    .wrapper {
        box-shadow: 0 0.2em 0.25em rgba(0, 0, 0, 0.8);
        box-sizing: border-rectangle;
        border-radius: 1em;
        background: white;
        padding: 0 1.2em;
        overflow: hidden;
        display: grid;
        height: 100%;
        width: 100%;
        position: relative;
    }
    
    .addEventButton,
    .calendarTextBlock,
    /* .eventButton, */
    .myEventsButton,
    .otherButton,.addEventButton2 {
        width: 280px; 
        height: 40px; 
        font-size: 16px;
        border-color: rgb(255, 255, 255);
        outline: 0.12rem solid rgb(255, 255, 255);
        background: rgba(175, 175, 175, 0.464); 
        color: black; 
        cursor: pointer;
        position: absolute; 
        left: 50%; 
        transform: translateX(-50%);
    }
  

    .addEventButton {
        top: 10px; 
    }

    .calendarTextBlock {
        top: 100px; 
        cursor: pointer;
    }

    .myEventsButton{
        top: 150px; 
        cursor: pointer; 
    }

    .otherButton {
        top: 200px;
        cursor: pointer; 
    }

    .addEventButton:hover {
        background: rgb(222, 232, 230);
    }
    .myEventsButton:hover {
        background: rgb(222, 232, 230);
    }
    .otherButton:hover {
        background: rgb(222, 232, 230);
    }

    .addEventButton2:hover {
        background: rgb(222, 232, 230);
    }

    /* Circle styles */
    .color-circle {
        width: 20px;
        height: 20px; 
        border-radius: 50%; 
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1; 
    }

    .my-events-circle {
        top: 160px; 
        left: 80px
    }

    .other-circle {
        top: 210px;
        left: 80px
    }

    .my-events-circle2 {
        top: 311px; 
        left: 62px
        
    }

</style>

<script>
    let isEventBoxActive = true;
    let isOtherBoxActive = false;

    function addEvent() {
        alert('Button clicked!');
    }

    function myEventsBox() {
        isEventBoxActive = !isEventBoxActive; 
        isOtherBoxActive = false; 
    }

    function otherBox() {
        isOtherBoxActive = !isOtherBoxActive; 
        isEventBoxActive = false; 
    }

    function Event() {
        alert('Button clicked!');
    }
</script>
