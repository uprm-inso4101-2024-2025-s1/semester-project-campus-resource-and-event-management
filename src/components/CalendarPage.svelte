<script>
    import RibbonComponent from "./RibbonCompenent.svelte";
    import MainCalendar from "./MainCalendar.svelte";
    let mainCalendarView = 'month'
</script>

<div class="layout">
    <div class="ribbonContainer">
        <RibbonComponent bind:mainCalendarView />
    </div>
    <div class="miniCalendarContainer"></div>
    <div class="AddEventSectionContainer"></div>
    <div class="mainCalendarContainer">
        <MainCalendar view={mainCalendarView} />
    </div>
</div>

<style>
    .layout {
        grid-template-columns: repeat(120, 1fr);
        grid-template-rows: repeat(120, 1fr);
        background: rgb(223, 223, 223);
        overflow: hidden;
        display: grid;
        height: 100%;
    }

    .ribbonContainer {
        grid-column: 2 / 120;
        grid-row: 3 / 10;
    }

    .mainCalendarContainer {
        grid-column: 40 / 119;
        grid-row: 12 / 119;
    }
</style>
