<div class="wrapper">
    {#if !isCreateEventActive}
        <button class="addEventButton" on:click={toggleEvent}>+ Add Event</button>
        
        <div class="color-circle my-events-circle" style="background-color: {isEventBoxActive ? 'green' : 'grey'};"></div>
        <button class="myEventsButton" on:click={myEventsBox}>My Events</button>

        <div class="color-circle other-circle" style="background-color: {isOtherBoxActive ? 'green' : 'grey'};"></div>
        <button class="otherButton" on:click={otherBox}>Other</button>
        
        <button class="calendarTextBlock">Calendar</button>
    {:else}
        <button class="goBackButton" on:click={toggleEvent}>&lt&lt&lt Go Back</button>
    {/if}
</div>

<style>
    .wrapper {
        box-shadow: 0 0.2em 0.25em rgba(0, 0, 0, 0.8);
        box-sizing: border-rectangle;
        border-radius: 1em;
        background: white;
        padding: 0 1.2em;
        overflow: hidden;
        display: grid;
        height: 83%;
        width: 30%;
        position: absolute;
        transform: translateY(-45%);
    }

    .addEventButton,
    .goBackButton,
    .calendarTextBlock,
    .myEventsButton,
    .otherButton {
        width: 280px; 
        height: 40px; 
        font-size: 16px;
        border-color: rgb(255, 255, 255);
        outline: 0.12rem solid rgb(255, 255, 255);
        background: white; 
        color: black; 
        cursor: pointer;
        position: absolute; 
        left: 50%; 
        transform: translateX(-50%);
    }

    .addEventButton {
        top: 10px; 
    }

    .goBackButton {
        top: 10px; 
    }

    .calendarTextBlock {
        top: 100px; 
        cursor: default;
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
    .goBackButton:hover {
        background: rgb(222, 232, 230);
    }
    .myEventsButton:hover {
        background: rgb(222, 232, 230);
    }
    .otherButton:hover {
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
</style>

<script>
  import App from "../App.svelte";

    let isEventBoxActive = true;
    let isOtherBoxActive = false;
    let isCreateEventActive = false;

    function toggleEvent() {
        isCreateEventActive = !isCreateEventActive;
    }

    function myEventsBox() {
        isEventBoxActive = !isEventBoxActive; 
        isOtherBoxActive = false; 
    }

    function otherBox() {
        isOtherBoxActive = !isOtherBoxActive; 
        isEventBoxActive = false; 
    }
</script>
