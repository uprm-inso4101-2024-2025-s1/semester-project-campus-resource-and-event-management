<script>
    // Placeholder data for events
    let events = [
        { id: 1, name: "Intro to Machine Learning Workshop", time: "10:00", place: "Colegio Room 101", creator: "Tech Club", rsvp: true, isFavorite: false, tags: ["Education", "Technology", "Workshop"],  },
        { id: 2, name: "Live Music and Food Festival", time: "18:00", place: "Central Park", creator: "Event Organizer", rsvp: false, isFavorite: false, tags: ["Entertainment", "Music", "Food"] },
        { id: 3, name: "Community Fun Run for Wellness", time: "07:00", place: "Colegio Stadium", creator: "Health Club", rsvp: false, isFavorite: false, tags: ["Health", "Sports"] },
        { id: 4, name: "Cultural Heritage Tour and Workshop", time: "09:00", place: "City Museum", creator: "History Department", rsvp: true, isFavorite: false, tags: ["Travel", "Education", "Workshop"] },
        { id: 5, name: "Electronic Music Production 101", time: "15:00", place: "Colegio Lab 5", creator: "Music Society", rsvp: true, isFavorite: false, tags: ["Music", "Technology"] },
        { id: 6, name: "Global Cuisine Tasting Event", time: "19:00", place: "Student Union", creator: "Foodies Club", rsvp: true, isFavorite: false, tags: ["Food", "Travel"] },
        { id: 7, name: "Charity Basketball Game and Halftime Show", time: "20:00", place: "Colegio Gym", creator: "Sports Association", rsvp: false, isFavorite: false, tags: ["Sports", "Entertainment"] },
        { id: 8, name: "Mindfulness and Stress-Relief Techniques Workshop", time: "14:00", place: "Colegio Wellness Center", creator: "Counseling Office", rsvp: true, isFavorite: false, tags: ["Health", "Workshop"] },
        { id: 9, name: "The History of Jazz: Lecture and Performance", time: "17:00", place: "Colegio Auditorium", creator: "Music Department", rsvp: true, isFavorite: false, tags: ["Education", "Music"] },
        { id: 10, name: "AI Ethics Panel Discussion", time: "11:00", place: "Conference Room B", creator: "Tech Ethics Committee", rsvp: true, isFavorite: false, tags: ["Education", "Technology"] },
        { id: 11, name: "Outdoor Yoga and Meditation Session", time: "06:30", place: "Campus Garden", creator: "Wellness Club", rsvp: false, isFavorite: false, tags: ["Health", "Sports"] },
        { id: 12, name: "Startup Pitch Night", time: "20:00", place: "Innovation Hub", creator: "Entrepreneurship Club", rsvp: true, isFavorite: false, tags: ["Technology", "Entertainment"] },
        { id: 13, name: "Open Mic Night", time: "19:30", place: "Student Cafe", creator: "Arts Society", rsvp: true, isFavorite: false, tags: ["Music", "Entertainment"] },
        { id: 14, name: "Study Abroad Information Session", time: "13:00", place: "Student Union Room 3", creator: "International Office", rsvp: true, isFavorite: false, tags: ["Travel", "Education"] },
        { id: 15, name: "Art Exhibition Opening", time: "16:00", place: "Colegio Art Gallery", creator: "Art Department", rsvp: false, isFavorite: false, tags: ["Entertainment", "Education"] },
        { id: 16, name: "Salsa Dancing Night", time: "21:00", place: "Community Hall", creator: "Dance Club", rsvp: true, isFavorite: false, tags: ["Entertainment", "Music"] },
        { id: 17, name: "Data Science Meetup", time: "18:00", place: "Library Conference Room", creator: "Tech Club", rsvp: true, isFavorite: false, tags: ["Education", "Technology"] },
        { id: 18, name: "Volunteer Beach Cleanup", time: "08:00", place: "Playa Grande", creator: "Environmental Club", rsvp: false, isFavorite: false, tags: ["Travel", "Health"] }
    ];

    let tags = [
        {name: "Education", selected: false},
        {name: "Entertainment", selected: false},
        {name: "Food", selected: false},
        {name: "Health", selected: false},
        {name: "Music", selected: false},
        {name: "Sports", selected: false},
        {name: "Technology", selected: false},
        {name: "Travel", selected: false},
        {name: "Workshop", selected: false}
    ];

    let selectedTags = [];

    // Function to generate a random color
    function getRandomColor() {
        const letters = "0123456789ABCDEF";
        let color = "#";
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    // Assign a random background to each event
    events = events.map(event => {
        return {
            ...event,
            showMore: false,
            dialog: null,
            bgColor: getRandomColor(),
        };
    });

    // Function to toggle the favorite state of a specific card
    function toggleFavorite(eventId) {
        events = events.map(event =>
            event.id === eventId ? { ...event, isFavorite: !event.isFavorite } : event
        );
    }

    function toggleSelect(tagName) {
        tags = tags.map(tag =>
            tag.name === tagName ? { ...tag, selected: !tag.selected } : tag
        );
        selectedTags = tags.filter(tag => tag.selected).map(tag => tag.name);
    }

    let searchQuery = "";
    let filteredEvents = events;

    // Function to filter events based on the search query
    function filterEvents() {
        filteredEvents = events.filter(event =>
            event.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
            event.tags.some(tag => tag.toLowerCase().includes(searchQuery.toLowerCase()))
        );
    }

    // Watch for changes in selected tags and filter events accordingly
    $: filteredEvents = selectedTags.length > 0 
        ? events.filter(event => selectedTags.every(tag => event.tags.includes(tag)))
        : events;


    let dialog;
    let showMoreA = false; // Global control for the modal
    let selectedEventId = null; // Track the selected event

    // Function to open dialog for a specific event
    function openDialog(eventId) {
        selectedEventId = eventId;
        // Update showMore for the specific event and reset the rest
        events = filteredEvents.map(event =>
        event.id === eventId ? { ...event, showMore: true } : { ...event, showMore: false }
        );
        showMoreA = true;
    }

    // Function to close dialog for a specific event
    function closeDialog(eventId) {
        events = filteredEvents.map(event =>
        event.id === eventId ? { ...event, showMore: false } : event
        );
        showMoreA = false;
        selectedEventId = null;
        dialog.close();
    }

    // Reactive statement to show the dialog when showMoreA is true
    $: if (dialog && showMoreA && selectedEventId !== null) {
        dialog.showModal();
        dialog.scrollTo(0, 0);
    }

</script>

<style>
    .dashboard {
        background: rgb(223, 223, 223);
        display: flex;
        flex-direction: column;
        gap: 1rem;
        padding: 1rem;
        padding-left: 2rem;
        font-family: "Roboto", sans-serif;
    }

    .search-container {
        display: flex;
        width: 100%;
        padding-bottom: 1rem;
        padding-top: 0.5rem;
    }

    .search-bar {
        display: flex;
        align-items: center; /* Align items vertically */
        padding-left: 40px; /* Add padding to leave space for the icon */
        position: relative; /* Set relative positioning for the container */
        width: 1359px; /* Make it take up all available space */
        height: 48px;
        max-width: none;
        border-radius: 8px;
        border: 1px solid #ccc;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .search-bar input {
        width: 100%; /* Full width input */
        padding: 0.5rem 1rem;
        font-size: 1rem;
        border: none; /* Remove extra border from the input */
        background-color: transparent; /* Input inherits the container background */
        color: black;
        border-radius: 8px;
        box-sizing: border-box;
    }

    .search-bar input:focus {
        outline: none; /* Remove default focus outline */
    }

    .search-bar::placeholder {
        color: gray; /* Optional: Placeholder text color */
        opacity: 0.7;
    }

    .search-bar svg.mag {
        position: absolute; /* Position the icon inside the container */
        left: 16px; /* Align it to the left with padding */
        top: 50%; /* Center vertically */
        transform: translateY(-50%); /* Offset to center the icon */
        width: 18px;
        height: 18px;
    }

    .search-bar svg.mic {
        position: absolute; /* Position the icon inside the container */
        right: 16px; /* Align it to the left with padding */
        top: 50%; /* Center vertically */
        transform: translateY(-50%); /* Offset to center the icon */
        width: 18px;
        height: 18px;
    }

    .content-container {
        display: flex;
        flex-direction: row;
        gap: 1rem;
    }

    .events-grid {
        flex: 1;
        display: grid;
        grid-template-columns: auto auto auto;
        grid-auto-rows: min-content;
        row-gap: 50px;
        column-gap: 48px;
        padding-right: 0.5rem;
    }

    .sidebar {
        background: white;
        border-left: 1px solid white;
        padding: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-radius: 20px;
        width: 241px;
        height: 1104px;
        padding-top: 1rem;
    }
    .sidebar ul {
        list-style: none;
        color: black;
    }

    .sidebar h3 {
        color: black;
        margin-bottom: 1rem;
        margin-left: 0.5rem;
        font-size: 20px;
        font-weight: 500;
        line-height: 28px;
        text-align: left;
    }

    .tag{
        border-radius: 5px;
        padding: 5px;
        cursor: pointer;
    }

    .tag.selected {
        background-color: #17c299;
        color: #053A2D;
    }

    .tag span {
        margin-left: 25px;
        margin-top: 2.5px;
        font-size: 14px;
        font-weight: 400;
        line-height: 20px;
    }

    .tag.content {
        display: flex;
    }

    .sidebar-grid {
        display: grid;
        grid-template-rows: auto;
        row-gap: 50px;
        column-gap: 48px;
        text-align: center;
        grid-gap: 10px;
    }

    .card {
        background: linear-gradient(to bottom, var(--bg-color) 194px, white 50%);
        border-radius: 20px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        width: 344px;
        height: 346px;
        border: none;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        overflow: hidden;
    }

    .card h3, p {
        color: black;
    }

    .content {
        height: 40%;
    }

    .profile-row {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }

    .profile-circle {
        width: 40px;
        height: 40px;
        background-color: var(--bg-color); /* Use the event color for the profile */
        filter: saturate(5);
        border-radius: 50%; /* Makes it a circle */
        flex-shrink: 0;
    }

    .event-title {
        display: flex;
        flex-direction: column;
    }

    h3 {
        margin: 0;
        font-size: 1.2rem; /* Default size */
        white-space: nowrap; /* Prevent text from wrapping */
        overflow: hidden; /* Hide overflowing text */
        text-overflow: ellipsis; /* Add ellipsis for overflowing text */
        display: block;
        transition: font-size 0.3s ease; /* Smooth resizing */
    }

    .creator {
        color: gray;
        font-size: 0.9rem;
        font-size: 14px;
        font-weight: 700;
        line-height: 20px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
    }

    p {
        margin: 0.5rem 0 1rem;
        color: gray;
        font-size: 14px;
        font-weight: 700;
        line-height: 20px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
    }

    .buttons {
        margin-top: auto;
        display: flex;
        gap: 15px;
        justify-content: space-between; /* Split content between left and right */
        align-items: center;
        width: 100%; /* Ensure buttons and icons stretch across the card's width */
    }

    button {
        background-color: transparent; /* Make the background transparent */
        border: none; /* Remove the border */
        color: inherit; /* Inherit the text color dynamically */
        cursor: pointer; 
        font-size: 14px;
        font-weight: 700;
        line-height: 24px;
        letter-spacing: 0.01em;
        text-align: center;
        padding: 5px;
        outline: none;
    }

    button:hover {
        text-decoration: underline; 
    }

    .left-buttons {
        display: flex;
        gap: 10px; /* Space between MORE and RSVP buttons */
    }

    .right-icons {
        display: flex;
        gap: 24px; /* Space between the favorite and more icons */
    }

    .icon {
        font-size: 24px; /* Adjust icon size */
        cursor: pointer;
        color: gray; /* Default icon color */
        transition: color 0.3s ease; /* Smooth transition */
    }

    .icon:hover {
        transform: scale(1.2);
    }

    dialog {
        width: 100%;
        max-width: 65rem;
        height: auto;
        border-radius: 20px;
        border: none;
        padding: 1.3rem;
        background-color: white;
        position: fixed;
        bottom: 0;
        margin-top: 10px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 10;
        overflow: auto;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
        animation: zoom-in 0.3s ease-out;
    }

    .event-details {
        margin-top: 10px;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

</style>

<div class="dashboard">
    <div class="search-container">
        <div class="search-bar">
            <svg  class="mag" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M11.965 11.255H12.755L17.745 16.255L16.255 17.745L11.255 12.755V11.965L10.985 11.685C9.845 12.665 8.365 13.255 6.755 13.255C3.165 13.255 0.255005 10.345 0.255005 6.755C0.255005 3.165 3.165 0.255005 6.755 0.255005C10.345 0.255005 13.255 3.165 13.255 6.755C13.255 8.365 12.665 9.845 11.685 10.985L11.965 11.255ZM2.255 6.755C2.255 9.245 4.26501 11.255 6.755 11.255C9.245 11.255 11.255 9.245 11.255 6.755C11.255 4.26501 9.245 2.255 6.755 2.255C4.26501 2.255 2.255 4.26501 2.255 6.755Z" fill="black" fill-opacity="0.6"/>
            </svg> 
            <input type="text" placeholder="Search for events..." bind:value="{searchQuery}" on:input="{filterEvents}" />
            <svg class="mic" width="14" height="20" viewBox="0 0 14 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M7 12.5C8.66 12.5 10 11.16 10 9.5V3.5C10 1.84 8.66 0.5 7 0.5C5.34 0.5 4 1.84 4 3.5V9.5C4 11.16 5.34 12.5 7 12.5ZM6 3.5C6 2.95 6.45 2.5 7 2.5C7.55 2.5 8 2.95 8 3.5V9.5C8 10.05 7.55 10.5 7 10.5C6.45 10.5 6 10.05 6 9.5V3.5ZM7 14.5C9.76 14.5 12 12.26 12 9.5H14C14 13.03 11.39 15.93 8 16.42V19.5H6V16.42C2.61 15.93 0 13.03 0 9.5H2C2 12.26 4.24 14.5 7 14.5Z" fill="black" fill-opacity="0.6"/>
            </svg>                               
        </div>
    </div>

    <div class="content-container">
        <!-- Event Cards Section -->
        <div class="events-grid">
            {#each filteredEvents as event}
                {#if selectedTags.length === 0 || event.tags.some(tag => selectedTags.includes(tag))}
                    <!-- Display the event card only if no tags are selected or if the event has at least one selected tag -->
                    <div class="card" style="--bg-color: {event.bgColor}">
                        <div class="content">
                            <div class="profile-row">
                                <div class="profile-circle"></div>
                                <div class="event-title">
                                    {#if event.name.length < 27}
                                        <h3>{event.name}</h3>
                                    {:else if event.name.length < 35}
                                        <h3 style="font-size: 1rem">{event.name}</h3>
                                    {:else if event.name.length < 42}
                                        <h3 style="font-size: 0.8rem; white-space: initial">{event.name}</h3>
                                    {:else}
                                        <h3 style="font-size: 0.6724rem; white-space: initial">{event.name}</h3>
                                    {/if}
                                    <div class="creator">by {event.creator}</div>
                                </div>
                            </div>
                            <p> Description: {event.time}, {event.place}</p>
                            <div class="buttons">
                                <div class="left-buttons" style="color: {event.bgColor}">
                                    <dialog bind:this={dialog}>
                                        <h2>{filteredEvents.find(event => event.id === selectedEventId)?.name}</h2>
                                        <p>{filteredEvents.find(event => event.id === selectedEventId)?.time}, {filteredEvents.find(event => event.id === selectedEventId)?.place}</p>
                                        <p>Hosted by {filteredEvents.find(event => event.id === selectedEventId)?.creator}</p>
                                        <div class="event-details">
                                          <p>RSVP: {filteredEvents.find(event => event.id === selectedEventId)?.rsvp ? "Yes" : "No"}</p>
                                          <p>Tags: {filteredEvents.find(event => event.id === selectedEventId)?.tags.join(", ")}</p>
                                          <p>Favorite: {filteredEvents.find(event => event.id === selectedEventId)?.isFavorite ? "Yes" : "No"}</p>
                                        </div>
                                        <button on:click={() => closeDialog(selectedEventId)}>Close</button>
                                    </dialog>
                                    {#if event.rsvp}
                                        <button on:click={() => openDialog(event.id)}>MORE</button>
                                        <button>RSVP</button>
                                    {:else}
                                        <button on:click={() => openDialog(event.id)}>MORE</button>
                                    {/if}
                                </div>

                                <div class="right-icons">
                                    <div class="icon favorite {event.isFavorite ? 'filled' : ''}" on:click={() => toggleFavorite(event.id)}>
                                        {#if event.isFavorite}
                                            <!-- Inline SVG for filled heart -->
                                            <svg width="24" height="24" viewBox="0 0 24 24" fill='none' xmlns="http://www.w3.org/2000/svg">
                                                <path d="M16.5 2.825C14.76 2.825 13.09 3.635 12 4.915C10.91 3.635 9.24 2.825 7.5 2.825C4.42 2.825 2 5.245 2 8.325C2 12.105 5.4 15.185 10.55 19.865L12 21.175L13.45 19.855C18.6 15.185 22 12.105 22 8.325C22 5.245 19.58 2.825 16.5 2.825Z" fill="{event.bgColor}"/>
                                            </svg>
                                                
                                        {:else}
                                            <!-- Inline SVG for heart outline -->
                                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path fill-rule="evenodd" clip-rule="evenodd" d="M12 4.915C13.09 3.635 14.76 2.825 16.5 2.825C19.58 2.825 22 5.245 22 8.325C22 12.1019 18.6056 15.1799 13.4627 19.8435L13.45 19.855L12 21.175L10.55 19.865L10.5105 19.8291C5.38263 15.1692 2 12.0953 2 8.325C2 5.245 4.42 2.825 7.5 2.825C9.24 2.825 10.91 3.635 12 4.915ZM12 18.475L12.1 18.375C16.86 14.065 20 11.215 20 8.325C20 6.325 18.5 4.825 16.5 4.825C14.96 4.825 13.46 5.815 12.94 7.185H11.07C10.54 5.815 9.04 4.825 7.5 4.825C5.5 4.825 4 6.325 4 8.325C4 11.215 7.14 14.065 11.9 18.375L12 18.475Z" fill="black" fill-opacity="0.6"/>
                                            </svg>
                                        {/if}
                                    </div>
                                    <span class="icon more">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path fill-rule="evenodd" clip-rule="evenodd" d="M12 8C13.1 8 14 7.1 14 6C14 4.9 13.1 4 12 4C10.9 4 10 4.9 10 6C10 7.1 10.9 8 12 8ZM12 10C10.9 10 10 10.9 10 12C10 13.1 10.9 14 12 14C13.1 14 14 13.1 14 12C14 10.9 13.1 10 12 10ZM10 18C10 16.9 10.9 16 12 16C13.1 16 14 16.9 14 18C14 19.1 13.1 20 12 20C10.9 20 10 19.1 10 18Z" fill="black" fill-opacity="0.6"/>
                                        </svg>
                                    </span>
                                </div>
            
                            </div>
                        </div>
                    </div>
                {/if}
            {/each}
        </div>

        <!-- Filter Panel -->
        <aside class="sidebar">
            <h3>Search by tag</h3>
            <ul>
                <div class="sidebar-grid">
                    {#each tags as tag}
                        <div class="tag {tag.selected ? 'selected' : ''}" on:click={() => toggleSelect(tag.name)}>
                            <div class="tag content">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" clip-rule="evenodd" d="M15.5 5C16.17 5 16.77 5.33 17.13 5.84L21.5 12L17.13 18.16C16.77 18.67 16.17 19 15.5 19L4.5 18.99C3.4 18.99 2.5 18.1 2.5 17V7C2.5 5.9 3.4 5.01 4.5 5.01L15.5 5ZM4.5 17H15.5L19.05 12L15.5 7H4.5V17Z" fill="black" fill-opacity="0.6"/>
                                </svg>
                                <span>{tag.name}</span>
                            </div>
                        </div>
                    {/each}
                </div>
            </ul>
        </aside>
    </div>
</div>
