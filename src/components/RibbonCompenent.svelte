<script>
    import App from "../App.svelte";
    export let mainCalendarView = 'month'
    import calendar_Img from "../assets/calendar.png"
</script>

<div class="Menu_bar">
    <button class="create_event" on:click={() => mainCalendarView = 'create_event'} class:currentView={mainCalendarView === 'create_event'}>CREATE EVENT</button>
    <button on:click={() => mainCalendarView = 'day'} class:currentView={mainCalendarView == 'day'}>Day</button>
    <button on:click={() => mainCalendarView = 'week'} class:currentView={mainCalendarView == 'week'}>Week</button>
    <button on:click={() => mainCalendarView = 'month'} class:currentView={mainCalendarView == 'month'} class="Calendar_Selection">Month</button>
    <img src={calendar_Img} alt="">
</div>

<style>
    .Menu_bar{
        background-color: white;
        position: relative;
        width: 100%;
        height: 50px;
        display:flex; 
        align-items: center;
        justify-content:flex-end;
        border-radius: 1.2em;
        gap: 34px;
        
    }

    .create_event{
        color: rgb(8, 94, 73);
        /* height: 75%; */
        margin-right: 51rem;
        border-radius: 30px;
        border-color: rgb(8, 94, 73);
        border-style: solid;
        padding: 8px;
        box-sizing: border-box;
        display: flex;
        font-size: small;
        /* border-color:; */
    
        /* border-radius: ; */
    }
    
    .Menu_bar img{
        height: 40px;
    }

    /* .Calendar_Selection{
        margin-right: 80px;
    } */
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