<script>
    import { getMonthName } from "../lib/calendarTools";
    import CalendarDay from "./CalendarDay.svelte";
    import CalendarHourMarkers from "./CalendarHourMarkers.svelte";

    export let currentDate
    export let currentMonth = currentDate.getMonth()
    export let currentYear = currentDate.getFullYear()

    export let calendarTitle
    export let events

    $: day = currentDate.getDate()
    $: isTodaysYear = currentYear == new Date().getFullYear()
    $: isTodaysMonth = currentMonth == new Date().getMonth()
    $: dayOfTheWeek = currentDate.getDay()
    let todaysDate = new Date().getDate();

    $: calendarTitle = `${getMonthName(currentDate.getMonth())} ${day} ${currentDate.getFullYear()}`

    // Scrolling the days
    export const scrollCalendar = (amt) => {
        currentDate.setDate(currentDate.getDate() + amt) // moving 1 day
        currentDate = currentDate
    } 

</script>

<div class="wrapper">
  <CalendarHourMarkers />

  <CalendarDay
    isDay={true}
    timed={true}
    {day}
    isCurrentDay={isTodaysMonth && isTodaysYear && day == todaysDate}
    events={events[day]}
  />
</div>

<style>
    .wrapper {
      grid-template: 1fr;
      position: relative;
      display: grid;
      height: 100%;
      width: 100%;
    }
</style>