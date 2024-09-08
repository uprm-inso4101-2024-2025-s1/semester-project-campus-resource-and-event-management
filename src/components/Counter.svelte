<script>
  import getServerData from '../lib/getTestServerData.js'

  let count = 0
  const increment = () => {
    count += 1
  }

  let serverData
</script>

<button on:click={increment}>
  count is {count}
</button>

<button on:click={() => getServerData().then(data => serverData = data)}>
  Get Data From Server
</button>

{#if serverData}
  <div>Fetched data: <span>{serverData}</span></div>
{/if}

<style>
  div {
    transform: translateX(-50%);
    position: absolute;
    margin-top: 0.5em;
    font-size: 1.2em;
    left: 50%;
  }

  span {
    color: green;
  }
</style>