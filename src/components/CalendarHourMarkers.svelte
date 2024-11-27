<div class="hoursWrapper">
  {#each [...Array(24).keys()] as h}
      <div class="hour" style={`grid-row: ${h+1};`}>{h}</div>
  {/each}
</div>

<style>
  .hoursWrapper {
      grid-template-rows: repeat(24, 1fr);
      pointer-events: none;
      margin-left: -1.2em;
      position: absolute;
      padding-top: 2em;
      display: grid;
      height: 100%;
      width: 1em;
      z-index: 1;
    }

    .hour {
      color: #777;
      text-align: center;
      line-height: 0;
    }
</style>