
  <script>
    import { getMonthName } from "../lib/calendarTools";
  
    export let currentDate = new Date();
    $: currentMonth = currentDate.getMonth();
    $: currentYear = currentDate.getFullYear();
    $: days = generateDays(currentYear, currentMonth);
  
    // Generate days for the calendar
    function generateDays(year, month) {
      let days = [];
      const firstDayOfMonth = new Date(year, month, 1).getDay();
      const lastDateOfMonth = new Date(year, month + 1, 0).getDate();
  
      // Add previous month's days
      const lastDateOfPrevMonth = new Date(year, month, 0).getDate();
      for (let i = firstDayOfMonth - 1; i >= 0; i--) {
        days.push({
          date: new Date(year, month - 1, lastDateOfPrevMonth - i),
          currentMonth: false,
        });
      }
  
      // Add current month's days
      for (let i = 1; i <= lastDateOfMonth; i++) {
        days.push({
          date: new Date(year, month, i),
          currentMonth: true,
        });
      }
  
      // Add next month's days
      const remainingDays = 42 - days.length; // 6 rows of 7 days
      for (let i = 1; i <= remainingDays; i++) {
        days.push({
          date: new Date(year, month + 1, i),
          currentMonth: false,
        });
      }
  
      return days;
    }
  
    // Scroll calendar by changing the month
    function scrollCalendar(offset) {
      currentDate = new Date(currentYear, currentMonth + offset, 1);
    }
  </script>

<div class="calendarWrapper">
  <!-- Header -->
  <div class="header">
    <h1>{getMonthName(currentMonth)} {currentYear}</h1>
    <div class="arrows">
      <button on:click={() => scrollCalendar(-1)}>&larr;</button>
      <button on:click={() => (currentDate = new Date())} class="todayBtn">TODAY</button>
      <button on:click={() => scrollCalendar(1)}>&rarr;</button>
    </div>
  </div>

  <!-- Days Row -->
  <div class="daysRow">
    {#each ["S", "M", "T", "W", "T", "F", "S"] as dayName}
      <div class="dayName">{dayName}</div>
    {/each}
  </div>

  <!-- Calendar Grid -->
  <div class="calendar-grid">
    {#each days as day}
      <div class="day {day.currentMonth ? '' : 'other-month'}">
        <span>{day.date.getDate()}</span>
      </div>
    {/each}
  </div>
</div>

<style>
  .calendarWrapper {
    box-shadow: 0 0.2em 0.25em rgba(0, 0, 0, 0.8);
      box-sizing: border-rectangle;
      border-radius: 1em;
      background: white;
      padding: 0 1.2em;
      overflow: hidden;
      display: grid;
      height: 100%;
      width: 100%;
      position: relative;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1em;
    color: rgb(51, 51, 51);
  }

  .arrows {
    display: flex;
    gap: 0.5em;
  }

  .arrows button:not(.todayBtn) {
    background-color: white;
    color: green;
  }

  .todayBtn {
    padding: 0.5em 1em;
    font-size: 12px;
    background-color: #00695c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .daysRow {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    margin-bottom: 0.5em;
    text-align: center;
  }

  .dayName {
    font-weight: bold;
    color: #555;
  }

  .calendar-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 0.5em;
  }

  .day {
    text-align: center;
    padding: 0.5em;
    background-color: #f9f9f9;
    border-radius: 4px;
    font-size: 13px;
    color: #333;
  }

  .day.other-month {
    color: grey;
  }

  .day span {
    display: inline-block;
    width: 2em;
    height: 2em;
    line-height: 2em;
    border-radius: 50%;
  }

  .day:hover span {
    background-color: #00695c;
    color: white;
  }
</style>

  