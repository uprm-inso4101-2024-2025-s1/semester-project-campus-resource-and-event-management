<script>
    import CalendarDay from "./CalendarDay.svelte";
    import { getDayOfTheWeekName, getMonthName } from "../lib/calendarTools";

    export let currentDate
    export let currentMonth = currentDate.getMonth()
    export let currentYear = currentDate.getFullYear()
  
    export let calendarTitle 
    $: sixDaysLater = new Date(currentDate)
    $: sixDaysLater.setDate(currentDate.getDate() + 6)

    $: isTodaysYear = currentYear == new Date().getFullYear()
    $: isTodaysMonth = currentMonth == new Date().getMonth()
    $: dayOfTheWeek = currentDate.getDay()

    // Scrolling the months
    export const scrollCalendar = (amt) => {
        currentDate.setDate(currentDate.getDate() + 7*amt) // skipping 7 days
        currentDate = currentDate
    } 
  
  // HARDCODED dummy data for monthly events
  const monthEvents = {
    2: [{ eventName: 'Event 1', startTime: 11, endTime: 13 }],
    6: [{ eventName: 'Event 1', startTime: 11, endTime: 13 }, { eventName: 'Event 2', startTime: 11, endTime: 13 }, { eventName: 'Event 3', startTime: 11, endTime: 13 }],
    10: [{ eventName: 'Event 1', startTime: 11, endTime: 13 }],
    17: [{ eventName: 'Event 1', startTime: 11, endTime: 13 }, { eventName: 'Event 2', startTime: 11, endTime: 13, noTagsInCommon: true }],
    28: [{ eventName: 'Event 1', startTime: 11, endTime: 13 }, { eventName: 'Event 2', startTime: 11, endTime: 13 }, { eventName: 'Event 3', startTime: 11, endTime: 13 }, { eventName: 'Event 3', startTime: 11, endTime: 13 }]
  }

  let days = Array(7)

  $: {
    days = [];
    let date = new Date(currentDate)

    // Adding days prior to today
    for(let i = dayOfTheWeek; i >= 0; i--) {
        const day = date.getDate()
        date.setDate(day - 1)
        days[i] = day
    }

    let sunday = new Date(date)
    sunday.setDate(sunday.getDate() + 1)
    
    // Adding days after today
    date = new Date(currentDate)
    for(let i = dayOfTheWeek; i < 7; i++) {
        const day = date.getDate()
        date.setDate(day + 1)
        days[i] = day
    }

    let saturday = new Date(date)
    saturday.setDate(saturday.getDate() - 1)

    calendarTitle = `${getMonthName(sunday.getMonth()).slice(0,3)} ${sunday.getDate()} ${sunday.getFullYear()} - ${getMonthName(saturday.getMonth()).slice(0,3)} ${saturday.getDate()} ${saturday.getFullYear()}`
  }

  let todaysDate = new Date().getDate();
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
  <div class="days">
      {#each days as day}
      {#key days}
        
      <CalendarDay
      isWeek={true}
      isNotFromMonth={false}
      {day}
      isCurrentDay={isTodaysMonth && isTodaysYear && day == todaysDate}
      events={monthEvents[day]}
      />
      {/key}
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

  .days {
      grid-template-columns: repeat(7, 1fr);
      background: rgb(175, 175, 175);
      box-sizing: border-box;
      padding: 0.12rem;
      overflow: hidden;
      display: grid;
      flex-grow: 1;
      gap: 0.12rem;
  }
</style>
