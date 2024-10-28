<script>
    import CalendarDay from "./CalendarDay.svelte";
    import { getDaysInMonth, getMonthName } from "../lib/calendarTools";

    export let currentDate
    export let currentMonth = currentDate.getMonth()
    export let currentYear = currentDate.getFullYear()

    $: daysInMonth = getDaysInMonth(currentMonth, currentYear)
    $: dayOffset = new Date(currentYear, currentMonth, 1).getDay()
    $: prevMonthDays = getDaysInMonth(currentMonth, currentYear)
    $: isTodaysMonth = currentMonth == new Date().getMonth()
    $: isTodaysYear = currentYear == new Date().getFullYear()
    
    export let calendarTitle 
    $: calendarTitle = `${getMonthName(currentMonth)} ${currentYear}`

    // Scrolling the months
    export const scrollCalendar = (amt) => {
        currentDate.setMonth(currentDate.getMonth()+amt)
        currentDate = currentDate
    } 
    
    // HARDCODED dummy data for monthly events
    const monthEvents = {
      2: [{ eventName: 'Event 1' }],
      6: [{ eventName: 'Event 1' }, { eventName: 'Event 2' }, { eventName: 'Event 3' }],
      10: [{ eventName: 'Event 1' }],
      17: [{ eventName: 'Event 1' }, { eventName: 'Event 2', noTagsInCommon: true }],
      28: [{ eventName: 'Event 1' }, { eventName: 'Event 2' }, { eventName: 'Event 3' }, { eventName: 'Event 3' }]
    }

    let prevDays = [];
    let days = [];
    let missingDays = [];
    let todaysDate = new Date().getDate();
    $: {
        prevDays = [];
        days = [];
        missingDays = [];
        for (
            let i = prevMonthDays - dayOffset + 1;
            i < prevMonthDays + 1;
            i++
        ) {
            prevDays.push(i);
        }
        for (let i = 1; i < daysInMonth + 1; i++) {
            days.push(i);
        }
        for (let i = 1; i < 43 - prevDays.length - days.length; i++) {
            missingDays.push(i);
        }
    }
</script>

<div class="wrapper">
    <div class="daysOfTheWeek">
        <p>SUN</p>
        <p>MON</p>
        <p>TUE</p>
        <p>WED</p>
        <p>THU</p>
        <p>FRI</p>
        <p>SAT</p>
    </div>
    <div class="daysOfTheMonth">
        {#each prevDays as day}
            <CalendarDay isNotFromMonth={true} {day} />
        {/each}
        {#each days as day}
            <CalendarDay
                {day}
                isCurrentDay={isTodaysYear && isTodaysMonth && day == todaysDate}
                events={monthEvents[day]}
            />
        {/each}
        {#each missingDays as day}
            <CalendarDay isNotFromMonth={true} {day} />
        {/each}
    </div>
</div>

<style>
    .wrapper {
        flex-direction: column;
        overflow: hidden;
        display: flex;
        height: 100%;
    }

    .daysOfTheWeek {
        justify-content: space-around;
        font-weight: 600;
        display: flex;
        margin: 0.5em;
        color: rgb(51, 51, 51);
    }

    p {
        margin: 0;
    }

    .daysOfTheMonth {
        grid-template-columns: repeat(7, 1fr);
        grid-template-rows: repeat(6, 1fr);
        background: rgb(175, 175, 175);
        box-sizing: border-box;
        padding: 0.12rem;
        overflow: hidden;
        display: grid;
        flex-grow: 1;
        gap: 0.12rem;
    }
</style>
