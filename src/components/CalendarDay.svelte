<script>
    import CalendarEvent from "./CalendarEvent.svelte";

    export let day;
    export let isCurrentDay = false;
    export let isNotFromMonth = false;
    export let events = [];
</script>

<div class="wrapper" class:isCurrentDay class:isNotFromMonth>
    <p class="day">{day}</p>

    {#each events as event}
        <CalendarEvent {event} />
    {/each}
</div>

<style>
    .wrapper {
        transition: background-color 0.125s;
        display: inline-block;
        background: white;
        cursor: pointer;
    }

    .wrapper:hover {
        background: rgb(222, 232, 230);
    }

    .isCurrentDay {
        outline: 0.2rem solid rgb(8, 94, 73);
        background: rgb(222, 232, 230);
        outline-offset: -0.2rem;
    }

    .isCurrentDay .day {
        color: rgb(8, 94, 73);
    }

    .isNotFromMonth {
        background: rgb(220, 220, 220);
    }

    .day {
        font-weight: 550;
        font-size: 1em;
        margin: 0.5em;
    }
</style>
