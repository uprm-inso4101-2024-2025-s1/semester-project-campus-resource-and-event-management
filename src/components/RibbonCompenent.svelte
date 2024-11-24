<script>
    export let mainCalendarView = 'month'
    export let createEvent = false
    import calendar_Img from "../assets/calendar.png"
</script>



<div class="Menu_bar">
    <button class="create_event" on:click={() => createEvent = true}>CREATE EVENT</button> 
    <button on:click={() => mainCalendarView = 'day'} class:currentView={mainCalendarView == 'day'}>Day</button>
    <button on:click={() => mainCalendarView = 'week'} class:currentView={mainCalendarView == 'week'}>Week</button>
    <button on:click={() => mainCalendarView = 'month'} class:currentView={mainCalendarView == 'month'} class="Calendar_Selection">Month</button>

    <div class="icon_container">
        <img src={calendar_Img} alt="Calendar Icon" class="icon_image">
    </div>
</div>


<style>
    .Menu_bar{
        background-color: white;
        position: relative;
        width: 100%;
        height: 100%;
        display:flex; 
        align-items: center;
        justify-content:flex-end;
        border-radius: 1.2em;
        gap: 34px;
        
    }

    .create_event{
        color: rgb(8, 94, 73);
        position: absolute;
        border-radius: 30px;
        border-color: rgb(8, 94, 73);
        border-style: solid;
        padding: 0 8px;
        height: 80%;
        box-sizing: border-box;
        display: flex;
        font-size: small;
        align-items: center;
        transition: 0.2s;
        left: 0.5em;
    }

    .create_event:hover {
        background-color: rgb(8, 94, 73); /* Green background on hover */
        color: white; /* White text on hover */
    }

    .icon_container {
        height: 100%;
    }
    
    .Menu_bar img{
        height: 100%;
    }

    button {
        all: unset;
        font-weight: bolder;
        user-select: none;
        cursor: pointer;
        color: black;
    }
    .currentView, button:hover{
        color: rgb(8, 94, 73);
    }

    

</style>