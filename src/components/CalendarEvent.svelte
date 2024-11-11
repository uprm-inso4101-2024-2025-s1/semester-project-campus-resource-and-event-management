<script>
  export let event
  export let timed
  let { noTagsInCommon, eventName } = event
</script>

<div class:timed class:noTagsInCommon class="eventWrapper" style={`grid-row: ${event.startTime}/${event.startTime + event.duration}`}>
  <span class="plusIcon">+</span>
  <span class="eventName">{eventName}</span>
</div>

<style>

  .eventWrapper {
    background: rgb(0, 120, 232);
    margin: 0 auto 0.4em auto;
    border-radius: 2em;
    font-size: 0.8em;
    padding: 0.2em;
    color: white;
    z-index: 1;
    width: 75%;
  }

  .timed {
    border-radius: 0.5em;
    width: 95%;
  }
  .noTagsInCommon {
    background: rgb(232, 0, 147);
  }

  .plusIcon {
    margin: 0 0.3em 0 0.6em;
    font-size: 1.2em;
    line-height: 0;
  }

</style>