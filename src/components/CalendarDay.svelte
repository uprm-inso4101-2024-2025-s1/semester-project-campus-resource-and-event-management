<script>
    import CalendarEvent from "./CalendarEvent.svelte";

    export let day;
    export let isCurrentDay = false;
    export let isNotFromMonth = false;
    export let timed = false;
    export let events = [];
</script>

<div class="dayWrapper" class:isCurrentDay class:isNotFromMonth>
    <p class="day">{day}</p>

    {#if timed}
        <div class="timeSlotsWrapper">
            {#each [...Array(24).keys()] as h}
                <div class="timeDivision" style={`grid-row: ${h};`}></div>
            {/each}
        </div>
    {/if}

    {#if events}
        <div class="events" class:timed>
            {#each events as event}
                <CalendarEvent {event} {timed} />
            {/each}
        </div>
    {/if}
</div>

<style>
    .dayWrapper {
        transition: background-color 0.125s;
        display: inline-block;
        background: white;
        position: relative;
        overflow-y: hidden;
        cursor: pointer;
    }

    .dayWrapper:hover {
        background: rgb(222, 232, 230);
    }

    .isCurrentDay {
        outline: 0.12rem solid rgb(8, 94, 73);
        background: rgb(222, 232, 230);
    }

    .isCurrentDay .day {
        color: rgb(8, 94, 73);
    }

    .isNotFromMonth {
        background: rgb(220, 220, 220);
    }

    .isNotFromMonth .day {
        color: rgb(129, 125, 125);
    }

    .day {
        color: #444;
        margin: 0.5em 0 0 0.5em;
        position: absolute;
        font-weight: 550;
        font-size: 1em;
        color: rgb(51, 51, 51);
    }

    .events {
        overflow: hidden;
        padding-top: 2em;
        height: 100%;
    }

    .events:hover {
        overflow-y: auto;
    }

    .timed {
        grid-template-rows: repeat(1440, 1fr);
        display: grid;
    }

    .timeSlotsWrapper {
        grid-template-rows: repeat(24, 1fr);
        position: absolute;
        padding-top: 2em;
        display: grid;
        height: 100%;
        width: 100%
    }

    .timeDivision {
        background: #E2E2E2;
        height: 1px;
    }

    .isCurrentDay .timeDivision {
        background: #C0C0C0;
    }
</style>
