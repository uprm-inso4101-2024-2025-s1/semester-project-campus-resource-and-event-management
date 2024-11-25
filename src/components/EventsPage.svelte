<script>
  import labelIcon from '../assets/label.png';

  let selectedTagId = 1; 
  let menuItems = [
    { id: 1, label: "Menu item 1" },
    { id: 2, label: "Menu item 2" },
    { id: 3, label: "Menu item 3" }
  ];
  let sectionItems1 = [
    { id: 4, label: "Menu item 1" },
    { id: 5, label: "Menu item 2" },
    { id: 6, label: "Menu item 3" }
  ];
  let sectionItems2 = [
    { id: 7, label: "Menu item 1" },
    { id: 8, label: "Menu item 2" },
    { id: 9, label: "Menu item 3" }
  ];
</script>

<div class="container">
  <div class="search-by-tag">
    <div class="header">
      <h4>Search by tag</h4>
      <p>Subtext</p>
    </div>

    <ul class="menu">
      {#each menuItems as item}
        <li
          class:active={selectedTagId === item.id}
          on:click={() => (selectedTagId = item.id)}
        >
          <img src="{labelIcon}" alt="icon" class="icon" />
          {item.label}
        </li>
      {/each}
    </ul>

    <hr class="divider" />

    <div class="section-header">Section header</div>
    <ul class="menu">
      {#each sectionItems1 as item}
        <li
          class:active={selectedTagId === item.id}
          on:click={() => (selectedTagId = item.id)}
        >
          <img src="{labelIcon}" alt="icon" class="icon" />
          {item.label}
        </li>
      {/each}
    </ul>

    <hr class="divider" />

    <ul class="menu">
      {#each sectionItems2 as item}
        <li
          class:active={selectedTagId === item.id}
          on:click={() => (selectedTagId = item.id)}
        >
          <img src="{labelIcon}" alt="icon" class="icon" />
          {item.label}
        </li>
      {/each}
    </ul>
  </div>
</div>

<style>
  .container {
    display: flex;
    justify-content: flex-end;
    padding: 16px;
    background-color: #D9D9D9;
    min-height: 100vh;
  }

  .search-by-tag {
    width: 260px;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    padding: 16px;
    font-family: 'Arial', sans-serif;
  }

  .header h4 {
    margin: 0;
    font-size: 16px;
    font-weight: bold;
    color: black;
  }

  .header p {
    margin: 4px 0 16px;
    font-size: 12px;
    color: #888;
  }

  .menu {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .menu li {
    display: flex;
    align-items: center;
    padding: 12px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    transition: background-color 0.2s, color 0.2s, border-color 0.2s;
    border: 1px solid transparent;
    color: black; 
  }

  .menu li .icon {
    width: 20px;
    height: 20px;
    margin-right: 12px;
  }

  .menu li.active {
    background-color: #00c48c;
    color: black; 
    border-color: #00c48c;
  }

  .menu li:hover {
    background-color: #f9f9f9;
    border-color: #e0e0e0;
  }

  .menu li.active:hover {
    background-color: #00c48c; 
    color: black;
    border-color: #00c48c;
  }

  .section-header {
    margin-top: 16px;
    margin-bottom: 8px;
    font-size: 14px;
    font-weight: bold;
    color: #444;
  }

  .divider {
    border: none;
    border-top: 1px solid #e0e0e0;
    margin: 16px 0;
  }
</style>
