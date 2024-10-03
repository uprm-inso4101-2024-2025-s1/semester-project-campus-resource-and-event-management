<script>
    import CalendarDay from "./CalendarDay.svelte";

  export const days = []
  export const month = 0 // january - december = 0 - 11

  for(let i = 1; i < 31; i++) { days.push(i) }
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
    {#each days as day}
      <CalendarDay {day} />
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
    grid-template-rows: repeat(5, 1fr);
    background: rgb(175, 175, 175);
    box-sizing: border-box;
    display: grid;
    height: 100%;
    gap: 0.12em;
  }

</style>