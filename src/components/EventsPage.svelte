<script>

  let items = [
      {
        id: 1,
        title: "Computer Science Engineering Conference",
        description: "A conference for UPRM computer science engineering students.",
        date: "2024-05-15",
        tags: ["tech", "conference", "AI"],
        rsvp: false,
        confirming: false,
      },
      {
        id: 2,
        title: "MUSA Fest",
        description: "Celebrating local art and culture.",
        date: "2024-06-10",
        tags: ["art", "festival"],
        rsvp:false,
        confirming: false,
      },
      {
        id: 3,
        title: "Music Night",
        description: "An evening of live music with la centenaria banda colegial.",
        date: "2024-07-05",
        tags: ["music", "concert", "live"],
        rsvp:false,
        confirming: false,
      },
      {
        id: 4,
        title: "Startup Competition",
        description: "Startup pitches.",
        date: "2024-05-20",
        tags: ["startup", "competition", "innovation"],
        rsvp:false,
        confirming: false,
      },
      {
        id: 5,
        title: "Health Workshop",
        description: "Mental wellness.",
        date: "2024-06-15",
        tags: ["health", "wellness"],
        rsvp:false,
        confirming: false,
      },
    ];
  
    let searchQuery = ""; 
    let filteredItems = []; 
    let selectedStartDate = "";
    let selectedEndDate = "";
  
   
    let selectedTags = [];
    let allTags = [...new Set(items.flatMap((item) => item.tags))];
  
  
// Notification messages
let successMessage = "";
let errorMessage = "";
let newEventTitle = "";
let newEventDescription = "";
let newEventDate = "";
let newEventTags = "";

function createEvent(title, description, date, tags) {
  // Check for missing fields
  if (!title || !description || !date || tags.length === 0) {
    errorMessage = "All fields are required to create an event.";
    successMessage = ""; // Clear success message
    displayNotification();
    return;
  }

  // Add the new event
  const newEvent = {
    id: items.length + 1,
    title,
    description,
    date,
    tags,
    rsvp: false,
    confirming: false,
  };

  items = [...items, newEvent];
  successMessage = "Event created successfully!";
  errorMessage = ""; // Clear error message
  displayNotification();

  // Reset form fields
  newEventTitle = "";
  newEventDescription = "";
  newEventDate = "";
  newEventTags = "";
}

// Function to display notifications
function displayNotification() {
  const notificationElement = document.querySelector(".notification");
  if (notificationElement instanceof HTMLElement) {
    notificationElement.style.display = "block";
    setTimeout(() => {
      notificationElement.style.display = "none";
    }, 3000); // Hide after 3 seconds
  }
}



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

    function toggleRSVP(itemId){
        items = items.map((item) =>
            item.id === itemId ? { ...item, confirming: !item.confirming } : item
        );
        filterItems(); 
    }

    function confirmRSVP(itemId){
        items = items.map((item) =>
            item.id === itemId ? { ...item, rsvp: true, confirming: false } : item
        );
        filterItems();
    }

    function cancelRSVP(itemId){
        items = items.map((item) =>
        item.id === itemId ? { ...item, rsvp: false, confirming: false } : item
    );
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
  </script>
  
  <div class="container">

    <div class="event-form">
      <h3>Create Event</h3>
      <input type="text" placeholder="Event Title" bind:value={newEventTitle} />
      <textarea placeholder="Event Description" bind:value={newEventDescription}></textarea>
      <input type="date" bind:value={newEventDate} />
      <input type="text" placeholder="Tags (comma separated)" bind:value={newEventTags} />
      <button on:click={() => createEvent(newEventTitle, newEventDescription, newEventDate, newEventTags.split(","))}>
        Create Event
      </button>
    </div>


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

    <div class="notification">
      {#if successMessage}
        <p class="success-message">{successMessage}</p>
      {/if}
      {#if errorMessage}
        <p class="error-message">{errorMessage}</p>
      {/if}
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

            {#if item.confirming}
                <button class="confirm-button" on:click={() => confirmRSVP(item.id)}>Confirm</button>
                <button class="cancel-button" on:click={() => cancelRSVP(item.id)}>Cancel</button>

            {:else}
                <button class="rsvp-button" on:click={() => toggleRSVP(item.id)}>
                  {item.rsvp ? "Cancel RSVP" : "RSVP"}
                </button>
            {/if}

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

    .event-card {
        margin-bottom: 16px;
        padding: 16px;
        background: #fff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .rsvp-button,
    .confirm-button,
    .cancel-button {
        margin-top: 8px;
        padding:8px 16px;
        border: none;
        border-radius: 4px;
        background-color: #00c48c;
        color: white;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .rsvp-button {
        background-color: #00c48c;
        color: white;
    }

    .confirm-button {
        background-color: #4caf50;
        color: white;
        margin-right: 8px;
    }

    .cancel-button {
        background-color: #f44336;
        color: white;
    }

    .rsvp-button:hover{
        background-color: #007a5e;
    }

    .confirm-button:hover {
        background-color: #388e3c;
    }
    .cancel-button:hover {
        background-color: #d32f2f;
    }


    .notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 12px 24px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: none;
  z-index: 1000;
}

.success-message {
  background-color: #4caf50;
  color: white;
}

.error-message {
  background-color: #f44336;
  color: white;
}

.event-form {
  margin-top: 16px;
  background: #fff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.event-form-container {
    width: 260px;
    margin-right: 16px;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    padding: 16px;
    font-family: 'Arial', sans-serif;
  }

  .event-form h3 {
    margin-bottom: 12px;
    font-size: 18px;
    color: black;
  }

.event-form input,
.event-form textarea {
  display: block;
  width: 100%;
  margin-bottom: 8px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}



.event-form button {
  padding: 8px 16px;
  background-color: #00c48c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.event-form button:hover {
  background-color: #007a5e;
}



  </style>
  