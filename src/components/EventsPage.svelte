<script>
    import iconSrc from '../assets/label_24px.png';
    let selectedTag = "Menu item 1";
    let menuItems = ["Menu item 1", "Menu item 2", "Menu item 3", "Menu item 4"];
  </script>
  
  <div class="container">
    <div class="search-by-tag">
      <div class="header">
        <h4>Search by tag</h4>
        <p>Subtext</p>
      </div>
      <ul class="menu">
        {#each menuItems as item}
          <li class:active={selectedTag === item} on:click={() => (selectedTag = item)}>
            <img src="{iconSrc}" alt="" class="icon" />
            {item}
          </li>
        {/each}
      </ul>
      <div class="section-header">Section header</div>
      <ul class="menu">
        {#each menuItems as item}
          <li class:active={selectedTag === item} on:click={() => (selectedTag = item)}>
            <img src="{iconSrc}" alt="" class="icon" />
            {item}
          </li>
        {/each}
      </ul>
    </div>
  </div>
  
  <style>
    /* Container to position search block to the right */
    .container {
      display: flex;
      justify-content: flex-end;
      padding: 16px;
      background-color: #D9D9D9;
      min-height: 100vh;
    }
  
    /* Search by tag block */
    .search-by-tag {
      width: 260px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      padding: 16px;
      font-family: 'Arial', sans-serif;
    }
  
    .header h4 {
      margin: 0;
      font-size: 14px;
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
      color: black;
    }
  
    .menu li {
      display: flex;
      align-items: center;
      padding: 8px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      transition: background-color 0.2s;
    }
  
    .menu li .icon {
      width: 16px;
      height: 16px;
      margin-right: 8px;
    }
  
    .menu li.active {
      background-color: #00c48c;
      color: #fff;
    }
  
    .section-header {
      margin-top: 16px;
      margin-bottom: 8px;
      font-size: 12px;
      font-weight: bold;
      color: #888;
    }
  </style>
  