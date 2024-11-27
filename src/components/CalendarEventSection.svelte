<div class="wrapper">
    <!-- Button to trigger adding a new event -->
    <button class="addEventButton" on:click={addEvent}>+ Add Event</button> 
    
    <!-- Indicator circle for "My Events" (green if active, grey if inactive) -->
    <div class="color-circle my-events-circle" style="background-color: {isEventBoxActive ? 'green' : 'grey'};"></div>
    <!-- Button to toggle the "My Events" filter -->
    <button class="myEventsButton" on:click={myEventsBox}>My Events</button>

    <!-- Indicator circle for "Other Events" (green if active, grey if inactive) -->
    <div class="color-circle other-circle" style="background-color: {isOtherBoxActive ? 'green' : 'grey'};"></div>
    <!-- Button to toggle the "Other Events" filter -->
    <button class="otherButton" on:click={otherBox}>Other</button>
    
    <!-- Static button for "Calendar" -->
    <button class="calendarTextBlock">Calendar</button>

    <!-- Display filtered events based on the active state -->
    <div class="events">
        {#each Object.entries(events) as [day, evs], day}
            {#each evs as event}
                {#if !event.noTagsInCommon && isEventBoxActive || 
                      !isEventBoxActive && event.noTagsInCommon || 
                      (!isEventBoxActive && !isOtherBoxActive)}
                    <!-- Render a CalendarEvent component for each event -->
                    <p><CalendarEvent {event} timed={false} /></p>
                {/if}
            {/each}
        {/each}
    </div>
</div>

<style>
    .wrapper {
        /* Main container with shadow, rounded corners, and padding */
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

    .wrapper::after {
        /* Adds a gradient overlay at the bottom */
        position: absolute;
        background: linear-gradient(rgba(0,0,0,0), white);
        height: 12.5%;
        content: "";
        width: 100%;
        bottom: 0;
    }
    
    /* Shared styles for buttons */
    .addEventButton,
    .calendarTextBlock,
    .myEventsButton,
    .otherButton {
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

    /* Specific positions for buttons */
    .addEventButton {
        top: 10px; 
    }

    .calendarTextBlock {
        top: 100px; 
        cursor: pointer;
    }

    .myEventsButton {
        top: 150px; 
        cursor: pointer; 
    }

    .otherButton {
        top: 200px;
        cursor: pointer; 
    }

    /* Hover effects for buttons */
    .addEventButton:hover {
        background: rgb(222, 232, 230);
    }
    .myEventsButton:hover {
        background: rgb(222, 232, 230);
    }
    .otherButton:hover {
        background: rgb(222, 232, 230);
    }

    /* Circular indicators for active/inactive states */
    .color-circle {
        width: 20px;
        height: 20px; 
        border-radius: 50%; 
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        z-index: 1; 
    }

    /* Position of the "My Events" indicator circle */
    .my-events-circle {
        top: 160px; 
        left: 80px
    }

    /* Position of the "Other Events" indicator circle */
    .other-circle {
        top: 210px;
        left: 80px
    }

    .events {
        /* Styles for the scrollable event list */
        position: absolute;
        overflow-y: auto;
        height: 32.5%;
        width: 100%;
        top:67.5%;
    }
</style>

<script>
    import CalendarEvent from "./CalendarEvent.svelte";

    // State for tracking the active filter
    let isEventBoxActive = true; // Whether "My Events" is active
    let isOtherBoxActive = false; // Whether "Other Events" is active
    export let events; // List of events to be rendered

    // Handles the "Add Event" button click
    function addEvent() {
        alert('Button clicked!');
    }

    // Toggles the "My Events" filter and deactivates the "Other" filter
    function myEventsBox() {
        isEventBoxActive = !isEventBoxActive; 
        isOtherBoxActive = false; 
    }

    // Toggles the "Other Events" filter and deactivates the "My Events" filter
    function otherBox() {
        isOtherBoxActive = !isOtherBoxActive; 
        isEventBoxActive = false; 
    }
</script>
