<script>
    import RibbonComponent from "./RibbonCompenent.svelte";
    import MainCalendar from "./MainCalendar.svelte";
</script>

<div class="layout">
    <div class="ribbonContainer">
        <RibbonComponent />
    </div>
    <div class="miniCalendarContainer"></div>
    <div class="AddEventSectionContainer"></div>
    <div class="mainCalendarContainer">
        <MainCalendar />
    </div>
</div>

<style>
    .layout {
        grid-template-columns: repeat(60, 1fr);
        grid-template-rows: repeat(60, 1fr);
        background: rgb(223, 223, 223);
        overflow: hidden;
        display: grid;
        height: 100%;
    }

    .mainCalendarContainer {
        grid-column: 20 / 60;
        grid-row: 6 / 60;
    }
</style>
