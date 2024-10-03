<script>
  export let event
  let { noTagsInCommon, eventName } = event
</script>

<div class:noTagsInCommon class="eventWrapper">
  <span class="plusIcon">+</span>
  <span class="eventName">{eventName}</span>
</div>

<style>

  .eventWrapper {
    background: rgb(0, 120, 232);
    margin: 0 auto 0.4em auto;
    border-radius: 2em;
    font-size: 0.8em;
    max-width: 75%;
    padding: 0.2em;
    color: white;
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