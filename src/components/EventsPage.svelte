<script>
    import EventsDashboard from "./EventsDashboard.svelte";

  let items = [
      {
        id: 1,
        title: "Computer Science Engineering Conference",
        description: "A conference for UPRM computer science engineering students.",
        date: "2024-05-15",
        tags: ["tech", "conference", "AI"],
      },
      {
        id: 2,
        title: "MUSA Fest",
        description: "Celebrating local art and culture.",
        date: "2024-06-10",
        tags: ["art", "festival"],
      },
      {
        id: 3,
        title: "Music Night",
        description: "An evening of live music with la centenaria banda colegial.",
        date: "2024-07-05",
        tags: ["music", "concert", "live"],
      },
      {
        id: 4,
        title: "Startup Competition",
        description: "Startup pitches.",
        date: "2024-05-20",
        tags: ["startup", "competition", "innovation"],
      },
      {
        id: 5,
        title: "Health Workshop",
        description: "Mental wellness.",
        date: "2024-06-15",
        tags: ["health", "wellness"],
      },
    ];
  
    let searchQuery = ""; 
    let filteredItems = []; 
    let selectedStartDate = "";
    let selectedEndDate = "";
  
   
    let selectedTags = [];
    let allTags = [...new Set(items.flatMap((item) => item.tags))];
  
  
    function filterItems() {
      const query = searchQuery.toLowerCase().trim();
  
      if (!query && !selectedStartDate && !selectedEndDate && selectedTags.length === 0) {
        filteredItems = []; 
          return;
      }
  
      filteredItems = items.filter((item) => {
        const matchesTitle = item.title.toLowerCase().includes(query);
        const matchesDescription = item.description.toLowerCase().includes(query);
        const matchesTags = selectedTags.length
          ? item.tags.some((tag) => selectedTags.includes(tag))
          : true;
  
        const matchesDate =
          (!selectedStartDate || new Date(item.date) >= new Date(selectedStartDate)) &&
          (!selectedEndDate || new Date(item.date) <= new Date(selectedEndDate));
  
    
        return (matchesTitle || matchesDescription || matchesTags) && matchesDate;
      });
    }
    function toggleTag(tag) {
      if (selectedTags.includes(tag)) {
        selectedTags = selectedTags.filter((selectedTag) => selectedTag !== tag);
      } else {
        selectedTags = [...selectedTags, tag];
      }
      filterItems();
    }
  
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
  <script/>

  <div>
    <EventsDashboard />
</div>
  
  <div class="container">
    <div class="page-header">
      <input
        type="text"
        placeholder="Search by keywords..."
        class="search-input"
        bind:value={searchQuery}
        on:input={filterItems}
      />
      <div class="date-filters">
        <label>Start Date:</label>
        <input type="date" bind:value={selectedStartDate} on:change={filterItems} />
        <label>End Date:</label>
        <input type="date" bind:value={selectedEndDate} on:change={filterItems} />
      </div>
    </div>
    <div class="event-list">
      {#if filteredItems.length > 0}
        {#each filteredItems as item}
          <div class="event-card">
            <h3>{item.title}</h3>
            <p>{item.description}</p>
            <p>Date: {item.date}</p>
            <div class="tags">
              {#each item.tags as tag}
                <span class="tag">{tag}</span>
              {/each}
            </div>
          </div>
        {/each}
      {:else if searchQuery.trim() !== ""}
        <p>No events match your search criteria.</p>
      {:else}
        <p>Start searching to view events!</p>
      {/if}
    </div>

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
      justify-content: space-between;
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
      align-self: flex-start;
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
    .page-header {
    position: relative; 
    color: black;
    margin-top: -650px;
    padding: 16px 24px;
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%; 
  }
  
  .search-input {
    flex: 1;
    padding: 12px;
    border: 1px solid #f9f9f9;
    border-radius: 4px;
    font-size: 14px;
    background-color: #f9f9f9;
    color: black;
  }
  
  .date-filters {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }
  
    .event-list {
      display:block;
      color: black;
      flex-direction:column;
      gap: 16px;
    }
  
  
    .event-card .tag {
      display: inline-block;
      padding: 6px 12px;
      margin: 4px 4px 0 0;
      background: #00c48c;
      color: #ffffff;
      border-radius: 8px;
      
    }
  </style>
  