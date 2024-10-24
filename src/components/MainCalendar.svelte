<script>
    import CalendarMonthView from "./CalendarMonthView.svelte";
    import { getDaysInMonth, getMonthName } from "../lib/calendarTools";
    export let view = "month";
    let todaysDate = new Date().getDate();


    let currentMonth = new Date().getMonth()+1;
    let currentYear = new Date().getFullYear();
    $: daysInMonth = getDaysInMonth(currentMonth, currentYear)
    $: dayOffset = new Date(currentYear, currentMonth-1, 1).getDay()
    $: prevMonthDays = getDaysInMonth(currentMonth-1, currentYear)
    $: isTodaysMonth = currentMonth == new Date().getMonth()+1

    function addMonth(amt) {
        var newMonth = currentMonth + amt;

        if (newMonth < 1) {
            currentYear -= 1;
            newMonth = 12;
        } else if (newMonth > 12) {
            currentYear += 1;
            newMonth = 1;
        }

        currentMonth = newMonth;
    }
</script>

<div class="wrapper">
    <h2>{getMonthName(currentMonth)} {currentYear}</h2>
    <div class="arrows">
        <button on:click={() => addMonth(-1)}>&lsaquo;</button>
        <button on:click={() => addMonth(1)}>&rsaquo;</button>
    </div>
    <div class="calendarViewWrapper">
        {#if view == "month"}
            <CalendarMonthView {daysInMonth} {dayOffset} {prevMonthDays} {isTodaysMonth} />
        {/if}
        {#if view == "day"}
            <p> October 28</p>
            <div class="day-event">
                <div>
                    <p>Event 1</p>
                </div>
                <div>
                    <p>Event 2</p>
                </div>
                <div>
                    <p>Event 3</p>
                </div>
                <div>
                    <p>Event 4</p>
                </div>
            </div>
        {/if}
    </div>
</div>

<style>
    .day-event {
        width: 80%;
        height: 50%;
        border-radius: 1px;
        background-color: rgb(210, 208, 206);
    }

    .day-event div {
        margin-bottom: 30px;
        width: 15%;
        border-style: solid;
        border-radius: 20px;
        background-color: rgb(0, 120, 232);
    }
    .wrapper p {
        color: rgb(0, 0, 0);
    }
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

    .arrows button {
        all: unset;
        height: 0;
        margin: 0 0.75em;
        cursor: pointer;
        color:rgb(51, 51, 51);
    }

    .arrows button:hover {
        color: rgb(8, 94, 73);
    }

    .calendarViewWrapper {
        grid-column: 1 / 11;
        grid-row: 3 / 20;
    }
</style>