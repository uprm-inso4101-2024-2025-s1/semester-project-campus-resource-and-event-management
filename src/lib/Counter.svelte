<script>
  let count = 0
  const increment = () => {
    count += 1
  }

  let serverData
  const getServerData = async () => {
    const response = await fetch('http://127.0.0.1:3451/api/')
    const textResponse = await response.text()
    serverData = textResponse
  }
</script>

<button on:click={increment}>
  count is {count}
</button>

<button on:click={getServerData}>
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