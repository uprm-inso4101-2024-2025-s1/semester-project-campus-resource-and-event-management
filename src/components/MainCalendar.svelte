<script>
    import CalendarMonthView from "./CalendarMonthView.svelte";
    import { getDaysInMonth, getMonthName } from "../lib/calendarTools";
    export const view = "month";

    let currentMonth = new Date().getMonth();
    let currentYear = new Date().getFullYear();
    $: daysInMonth = getDaysInMonth(currentMonth, currentYear)
    $: dayOffset = new Date(currentYear, currentMonth-1, 1).getDay()
    $: prevMonthDays = getDaysInMonth(currentMonth-1, currentYear)

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
            <CalendarMonthView {daysInMonth} {dayOffset} {prevMonthDays} />
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
        display: grid;
        height: 100%;
        width: 100%;
    }

    h2 {
        grid-column: 1 / 6;
        grid-row: 2 / 3;
        font-weight: 800;
        line-height: 0;
    }

    .arrows {
        justify-content: space-between;
        grid-column: 10 / 11;
        user-select: none;
        padding: 0 0.75em;
        grid-row: 2 / 3;
        font-size: 2em;
        line-height: 0;
        display: flex;
    }

    .arrows button {
        all: unset;
        cursor: pointer;
    }

    .arrows button:hover {
        color: rgb(8, 94, 73);
    }

    .calendarViewWrapper {
        grid-column: 1 / 11;
        grid-row: 3 / 20;
    }
</style>
