<script>
    import CalendarMonthView from "./CalendarMonthView.svelte";
    import CalendarWeekView from "./CalendarWeekView.svelte";
    import CalendarDailyView from "./CalendarDailyView.svelte";
    export let view = "month";
    export let events
    
    let currentDate = new Date();
    $: currentMonth = currentDate.getMonth()
    $: currentYear = currentDate.getFullYear()

    let scrollCalendar
    let calendarTitle
</script>

<div class="wrapper">
    <h2>{calendarTitle}</h2>
    <div class="arrows">
        <button on:click={() => currentDate = new Date()} class="todayBtn">TODAY</button>
        <button on:click={() => scrollCalendar(-1)}>&lsaquo;</button>
        <button on:click={() => scrollCalendar(1)}>&rsaquo;</button>
    </div>
    <div class="calendarViewWrapper">
        {#if view == "month"}
            <CalendarMonthView bind:scrollCalendar bind:calendarTitle bind:currentDate {currentMonth} {currentYear} {events} />
        {:else if view == "week"}
            <CalendarWeekView bind:scrollCalendar bind:calendarTitle bind:currentDate {currentMonth} {currentYear} {events} />
        {:else if view == "day"}
            <CalendarDailyView bind:scrollCalendar bind:calendarTitle bind:currentDate {currentMonth} {currentYear} {events} />
        {/if}
    </div>
</div>

<style>
    .wrapper {
        box-shadow: 0 0.2em 0.25em rgba(0, 0, 0, 0.8);
        grid-template-columns: repeat(10, 1fr);
        grid-template-rows: repeat(20, 1fr);
        box-sizing: border-box;
        border-radius: 1em;
        background: white;
        padding: 0 1.2em;
        overflow: hidden;
        display: grid;
        height: 100%;
        width: 100%;
    }

    h2 {
        grid-column: 1 / 6;
        grid-row: 2 / 3;
        font-weight: 800;
        line-height: 0;
        color: rgb(51, 51, 51);
    }

    .arrows {
        justify-content: center;
        grid-column: 10 / 11;
        user-select: none;
        grid-row: 2 / 3;
        font-size: 2em;
        line-height: 0;
        display: flex;
    }

    .arrows button:not(.todayBtn) {
        all: unset;
        height: 0;
        margin: 0 0.75em;
        cursor: pointer;
        color:rgb(51, 51, 51);
    }

    .arrows button:hover {
        color: rgb(8, 94, 73);
    }

    .todayBtn {
        all: unset;
        border: 1.25px solid currentColor;
        margin: -1.25em 0.75em 0 0;
        border-radius: 5em;
        font-weight: bold;
        user-select: none;
        font-size: 0.8rem;
        cursor: pointer;
        padding: 0 1.5em;
        height: 2.8em;
        color: rgb(8, 94, 73);
    }

    .calendarViewWrapper {
        grid-column: 1 / 11;
        grid-row: 3 / 20;
    }
</style>