<script>
    import CalendarDay from "./CalendarDay.svelte";
    export let prevMonthDays;
    export let isTodaysMonth;
    export let daysInMonth;
    export let dayOffset;
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
                isCurrentDay={isTodaysMonth && day == todaysDate}
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
        display: flex;
        height: 100%;
    }

    .daysOfTheWeek {
        justify-content: space-around;
        font-weight: 600;
        display: flex;
        margin: 0.5em;
    }

    p {
        margin: 0;
    }

    .daysOfTheMonth {
        border: 0.12em solid rgb(175, 175, 175);
        grid-template-columns: repeat(7, 1fr);
        grid-template-rows: repeat(6, 1fr);
        background: rgb(175, 175, 175);
        box-sizing: border-box;
        display: grid;
        height: 100%;
        gap: 0.12em;
    }
</style>
