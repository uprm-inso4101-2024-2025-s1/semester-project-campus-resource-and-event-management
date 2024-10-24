<script>
  import CalendarDay from "./CalendarDay.svelte";
  import { getDaysInMonth, getMonthName } from "../lib/calendarTools";

  let currentMonth = new Date().getMonth()+1;
  let currentYear = new Date().getFullYear();

  $: daysInMonth = getDaysInMonth(currentMonth, currentYear)
  $: dayOffset = new Date(currentYear, currentMonth-1, 1).getDay()
  $: prevMonthDays = getDaysInMonth(currentMonth-1, currentYear)
  
  export let calendarTitle 
  $: calendarTitle = `` // TODO

  // Scrolling the months
  export const scrollCalendar = (amt) => {
      // TODO
  } 
  
  // HARDCODED dummy data for monthly events
  const monthEvents = {
    2: [{ eventName: 'Event 1' }],
    6: [{ eventName: 'Event 1' }, { eventName: 'Event 2' }, { eventName: 'Event 3' }],
    10: [{ eventName: 'Event 1' }],
    17: [{ eventName: 'Event 1' }, { eventName: 'Event 2', noTagsInCommon: true }],
    28: [{ eventName: 'Event 1' }, { eventName: 'Event 2' }, { eventName: 'Event 3' }, { eventName: 'Event 3' }]
  }

  let days = [];
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
          <CalendarDay
              isNotFromMonth={false}
              {day}
              isCurrentDay={false}
              events={monthEvents[day]}
          />
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
