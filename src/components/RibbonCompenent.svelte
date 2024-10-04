<script>
    export let mainCalendarView = 'month'
</script>

<div class="Menu_bar">
    <button on:click={() => mainCalendarView = 'day'} class:currentView={mainCalendarView == 'day'}>Day</button>
    <button on:click={() => mainCalendarView = 'week'} class:currentView={mainCalendarView == 'week'}>Week</button>
    <button on:click={() => mainCalendarView = 'month'} class:currentView={mainCalendarView == 'month'} class="Calendar_Selection">Month</button>
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
    .Calendar_Selection{
        margin-right: 80px;
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