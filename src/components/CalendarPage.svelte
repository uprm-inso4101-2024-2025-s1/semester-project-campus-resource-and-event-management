<script>
    import RibbonComponent from "./RibbonCompenent.svelte";
    import MainCalendar from "./MainCalendar.svelte";
    import EventSection from "./CalendarEventSection.svelte";
    import MiniCalendar from "./MiniCalendar.svelte";
    let mainCalendarView = 'month'

    // HARDCODED dummy data for events
    let events = {
      2: [{ eventName: 'Event 1', startTime: 0, duration: 3*60 }],
      6: [{ eventName: 'Event 1', startTime: 11*60, duration: 3*60 }, { eventName: 'Event 2', startTime: 12*60, duration: 3*60 }, { eventName: 'Event 3', startTime: 13*60, duration: 3*60 }],
      10: [{ eventName: 'Event 1', startTime: 11*60, duration: 3*60 }],
      17: [{ eventName: 'Event 1', startTime: 11*60, duration: 3*60 }, { eventName: 'Event 2', startTime: 11*60, duration: 3*60, noTagsInCommon: true }],
      28: [{ eventName: 'Event 1', startTime: 11*60, duration: 3*60 }, { eventName: 'Event 2', startTime: 11*60, duration: 3*60 }, { eventName: 'Event 3', startTime: 11*60, duration: 3*60 }, { eventName: 'Event 3', startTime: 11*60, duration: 3*60 }]
    }
</script>

<div class="layout">
    <div class="ribbonContainer">
        <RibbonComponent bind:mainCalendarView />
    </div>
    <div class="eventContainer">
        <EventSection bind:events/>
    </div>
    <div class="miniCalendarContainer">
        <MiniCalendar/>
    </div>
    <div class="AddEventSectionContainer"></div>
    <div class="mainCalendarContainer">
        <MainCalendar view={mainCalendarView} bind:events />
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

    .eventContainer {
        grid-column: 3 / 38;
        grid-row: 60 / 119;
    }

    .miniCalendarContainer {
        grid-column: 3 / 38;
        grid-row: 12 / 57;
    }
</style>
