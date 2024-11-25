<script>
    // Placeholder data for events
    let events = [
        { id: 1, name: "Intro to Machine Learning Workshop", time: "10:00", place: "Colegio Room 101", creator: "Tech Club", rsvp: true, isFavorite: false, tags: ["Education", "Technology", "Workshop"], description: "", seats: 30, rsvpList: []  },
        { id: 2, name: "Live Music and Food Festival", time: "18:00", place: "Central Park", creator: "Event Organizer", rsvp: false, isFavorite: false, tags: ["Entertainment", "Music", "Food"], description: "" },
        { id: 3, name: "Community Fun Run for Wellness", time: "07:00", place: "Colegio Stadium", creator: "Health Club", rsvp: false, isFavorite: false, tags: ["Health", "Sports"], description: "" },
        { id: 4, name: "Cultural Heritage Tour and Workshop", time: "09:00", place: "City Museum", creator: "History Department", rsvp: true, isFavorite: false, tags: ["Travel", "Education", "Workshop"], description: "", seats: 30, rsvpList: [] },
        { id: 5, name: "Electronic Music Production 101", time: "15:00", place: "Colegio Lab 5", creator: "Music Society", rsvp: true, isFavorite: false, tags: ["Music", "Technology"], description: "", seats: 30, rsvpList: [] },
        { id: 6, name: "Global Cuisine Tasting Event", time: "19:00", place: "Student Union", creator: "Foodies Club", rsvp: true, isFavorite: false, tags: ["Food", "Travel"], description: "", seats: 30, rsvpList: [] },
        { id: 7, name: "Charity Basketball Game and Halftime Show", time: "20:00", place: "Colegio Gym", creator: "Sports Association", rsvp: false, isFavorite: false, tags: ["Sports", "Entertainment"], description: "" },
        { id: 8, name: "Mindfulness and Stress-Relief Techniques Workshop", time: "14:00", place: "Colegio Wellness Center", creator: "Counseling Office", rsvp: true, isFavorite: false, tags: ["Health", "Workshop"], description: "", seats: 30, rsvpList: [] },
        { id: 9, name: "The History of Jazz: Lecture and Performance", time: "17:00", place: "Colegio Auditorium", creator: "Music Department", rsvp: true, isFavorite: false, tags: ["Education", "Music"], description: "",seats: 30, rsvpList: [] },
        { id: 10, name: "AI Ethics Panel Discussion", time: "11:00", place: "Conference Room B", creator: "Tech Ethics Committee", rsvp: true, isFavorite: false, tags: ["Education", "Technology"], description: "", seats: 30, rsvpList: [] },
        { id: 11, name: "Outdoor Yoga and Meditation Session", time: "06:30", place: "Campus Garden", creator: "Wellness Club", rsvp: false, isFavorite: false, tags: ["Health", "Sports"], description: "" },
        { id: 12, name: "Startup Pitch Night", time: "20:00", place: "Innovation Hub", creator: "Entrepreneurship Club", rsvp: true, isFavorite: false, tags: ["Technology", "Entertainment"], description: "", seats: 30, rsvpList: [] },
        { id: 13, name: "Open Mic Night", time: "19:30", place: "Student Cafe", creator: "Arts Society", rsvp: true, isFavorite: false, tags: ["Music", "Entertainment"], description: "", seats: 30, rsvpList: [] },
        { id: 14, name: "Study Abroad Information Session", time: "13:00", place: "Student Union Room 3", creator: "International Office", rsvp: true, isFavorite: false, tags: ["Travel", "Education"], description: "", seats: 30, rsvpList: [] },
        { id: 15, name: "Art Exhibition Opening", time: "16:00", place: "Colegio Art Gallery", creator: "Art Department", rsvp: false, isFavorite: false, tags: ["Entertainment", "Education"], description: "" },
        { id: 16, name: "Salsa Dancing Night", time: "21:00", place: "Community Hall", creator: "Dance Club", rsvp: true, isFavorite: false, tags: ["Entertainment", "Music"], description: "", seats: 30, rsvpList: [] },
        { id: 17, name: "Data Science Meetup", time: "18:00", place: "Library Conference Room", creator: "Tech Club", rsvp: true, isFavorite: false, tags: ["Education", "Technology"], description: "", seats: 30, rsvpList: [] },
        { id: 18, name: "Volunteer Beach Cleanup", time: "08:00", place: "Playa Grande", creator: "Environmental Club", rsvp: false, isFavorite: false, tags: ["Travel", "Health"], description: "" }
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
        {name: "Workshop", selected: false},
        {name: "Favorites", selected: false }
    ];

    let selectedTags = [];
    let searchQuery = "";
    let filteredEvents = events;
    let selectedEvent = null; 
    let selectedRSVPEvent = null;
    let userName = "";
    let userEmail = "";
    let confirmationMessage = "";


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
            bgColor: getRandomColor(),
        };
    });


    // Function to toggle the favorite state of a specific card
    function toggleFavorite(eventId) {
        events = events.map(event =>
            event.id === eventId ? { ...event, isFavorite: !event.isFavorite } : event
        );
        const event = events.find(event => event.id === eventId);
        if (event.isFavorite)
            event.tags.push("Favorites");
        else
            event.tags.splice(event.tags.indexOf("Favorites"), 1);
        // Trigger reactivity for `events` and `filteredEvents`
        events = [...events];
        filterEvents();
    }

    function toggleSelect(tagName) {
        tags = tags.map(tag =>
            tag.name === tagName ? { ...tag, selected: !tag.selected } : tag
        );
        selectedTags = tags.filter(tag => tag.selected).map(tag => tag.name);
        filterEvents(); // Trigger filtering after toggling tags
    }

    // Function to filter events based on the search query
    function filterEvents() {
        if (selectedTags.length > 0) {
            filteredEvents = events.filter(event =>
                selectedTags.every(tag => event.tags.includes(tag))
            );
        } else {
            // No tags selected, show all events
            filteredEvents = events;
        }

        // Apply search query filtering
        if (searchQuery) {
            filteredEvents = filteredEvents.filter(event =>
                event.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                event.creator.toLowerCase().includes(searchQuery.toLowerCase()) ||
                event.time.toLowerCase().includes(searchQuery.toLowerCase()) ||
                event.place.toLowerCase().includes(searchQuery.toLowerCase())
            );
        }
    }
    // Watch for changes in selected tags and filter events accordingly
    $: filterEvents();

    // Function to open dialog and load description
    async function openDialog(event) {
        selectedEvent = { ...event }; // Clone event to avoid mutating original
        const description = await loadDescriptionFromFile(event.id);
        selectedEvent.description = description;
        document.body.classList.add("no-scroll");
    }

    function closeDialog() {
        selectedEvent = null;
        document.body.classList.remove("no-scroll"); 
    }

    // Function to load description from a file
   // Fetch the description from the JSON file
   async function loadDescriptionFromFile(eventId) {
        try {
            const response = await fetch('/src/lib/descriptions.json'); // Adjust path if necessary
            const descriptions = await response.json();
            return descriptions[eventId] || "No description available.";
        } catch (error) {
            console.error("Error loading description:", error);
            return "An error occurred while loading the description.";
        }
    }

    $: tags = tags.map(tag => ({
        ...tag,
        class: tag.name === 'Entertainment' ? 'entertainment-tag' : ''
    }));

    function openRSVPPopup(event) {
        selectedRSVPEvent = event;
        userName = "";
        userEmail = "";
        confirmationMessage = "";
        document.body.classList.add("no-scroll");
    }

    function closeRSVPPopup() {
        selectedRSVPEvent = null;
        document.body.classList.remove("no-scroll");
    }

    function handleRSVP() {
        if (!userName || !userEmail) {
            confirmationMessage = "Please fill in both name and email.";
            return;
        }

        if (selectedRSVPEvent) {
            selectedRSVPEvent.rsvpList.push({ name: userName, email: userEmail });
            selectedRSVPEvent.seats--;
            confirmationMessage = `You have successfully RSVP'd for ${selectedRSVPEvent.name}.`;
        }
    }

    function cancelRSVP(event) {
        const userIndex = event.rsvpList.findIndex(user => user.email === userEmail);
        if (userIndex !== -1) {
            event.rsvpList.splice(userIndex, 1);
            event.seats++;
        }
    }

    function toggleRSVP(event) {
        const userRegistered = event.rsvpList.some(user => user.email === userEmail);
        if (userRegistered) {
            cancelRSVP(event);
        } else {
            openRSVPPopup(event);
        }
    }
</script>

<div class="dashboard">
    <div class="search-container">
        <div class="search-bar">
            <svg  class="mag" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M11.965 11.255H12.755L17.745 16.255L16.255 17.745L11.255 12.755V11.965L10.985 11.685C9.845 12.665 8.365 13.255 6.755 13.255C3.165 13.255 0.255005 10.345 0.255005 6.755C0.255005 3.165 3.165 0.255005 6.755 0.255005C10.345 0.255005 13.255 3.165 13.255 6.755C13.255 8.365 12.665 9.845 11.685 10.985L11.965 11.255ZM2.255 6.755C2.255 9.245 4.26501 11.255 6.755 11.255C9.245 11.255 11.255 9.245 11.255 6.755C11.255 4.26501 9.245 2.255 6.755 2.255C4.26501 2.255 2.255 4.26501 2.255 6.755Z" fill="black" fill-opacity="0.6"/>
            </svg> 
            <input type="text" placeholder="Search for..." bind:value="{searchQuery}" on:input="{filterEvents}" />
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
                                    {#if event.rsvp}
                                        <button on:click={() => openDialog(event)}>MORE</button>
                                        <button on:click={() => openRSVPPopup(event)}>
                                            {event.rsvpList.some(user => user.email === userEmail) ? "Cancel RSVP" : "RSVP"}
                                        </button>
                                    {:else}
                                        <button on:click={() => openDialog(event)}>MORE</button>
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
        <!-- Dialog for event details -->
        {#if selectedEvent}
            <dialog open style="color: {selectedEvent.bgColor}" on:click={closeDialog}>
                <div class="modal-content" on:click|stopPropagation>
                    <div class="modal-left">
                        <h2>{selectedEvent.name}</h2>
                        <p>{selectedEvent.time}, {selectedEvent.place}</p>
                        <p>Hosted by {selectedEvent.creator}</p>
                        <div class="event-details">
                            <p>RSVP: {selectedEvent.rsvp ? "Yes" : "No"}</p>
                            <p>|</p>
                            <p>Tags: {selectedEvent.tags.join(", ")}</p>
                            <p>|</p>
                            <p>Favorite: {selectedEvent.isFavorite ? "Yes" : "No"}</p>
                        </div>
                        <a>{selectedEvent.description || "Loading description..."}</a>
                        <div class="modal-footer">
                            <button on:click={closeDialog}>Close</button>
                        </div>
                    </div>
                    <div class="modal-right">
                        <div class="event-image" style="background: {selectedEvent.bgColor};">
                            <!-- Placeholder for event image -->
                        </div>
                    </div>
                </div>
            </dialog>
        {/if}

        <!-- RSVP Pop-Up -->
        {#if selectedRSVPEvent}
            <dialog open class="rsvp-popup" style="color: {selectedRSVPEvent.bgColor}" on:click={closeRSVPPopup}>
                <div class="rsvp-content" on:click|stopPropagation>
                    <h2>RSVP for {selectedRSVPEvent.name}</h2>
                    <p>{selectedRSVPEvent.time}, {selectedRSVPEvent.place}</p>
                    <form on:submit|preventDefault={handleRSVP}>
                        <label>
                            Name:
                            <input type="text" bind:value={userName} placeholder="Enter your name" />
                        </label>
                        <label>
                            Email:
                            <input type="email" bind:value={userEmail} placeholder="Enter your email" />
                        </label>
                        <button type="submit">Submit RSVP</button>
                    </form>
                    {#if confirmationMessage}
                        <p class="confirmation">{confirmationMessage}</p>
                    {/if}
                    <button on:click={closeRSVPPopup}>Close</button>
                </div>
            </dialog>
        {/if}

        <!-- Filter Panel -->
        <aside class="sidebar">
            <h3>Search by tag</h3>
            <ul>
                <div class="sidebar-grid">
                    {#each tags as tag}
                        <div class="tag {tag.name === 'Entertainment' ? 'entertainment-tag' : ''} {tag.selected ? 'selected' : ''}" on:click={() => toggleSelect(tag.name)}>
                            <div class="tag content">
                                {#if tag.name === "Favorites"}
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd" clip-rule="evenodd" d="M12 4.915C13.09 3.635 14.76 2.825 16.5 2.825C19.58 2.825 22 5.245 22 8.325C22 12.1019 18.6056 15.1799 13.4627 19.8435L13.45 19.855L12 21.175L10.55 19.865L10.5105 19.8291C5.38263 15.1692 2 12.0953 2 8.325C2 5.245 4.42 2.825 7.5 2.825C9.24 2.825 10.91 3.635 12 4.915ZM12 18.475L12.1 18.375C16.86 14.065 20 11.215 20 8.325C20 6.325 18.5 4.825 16.5 4.825C14.96 4.825 13.46 5.815 12.94 7.185H11.07C10.54 5.815 9.04 4.825 7.5 4.825C5.5 4.825 4 6.325 4 8.325C4 11.215 7.14 14.065 11.9 18.375L12 18.475Z" fill="black" fill-opacity="0.6"/>
                                    </svg>
                                {:else}
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path fill-rule="evenodd" clip-rule="evenodd" d="M15.5 5C16.17 5 16.77 5.33 17.13 5.84L21.5 12L17.13 18.16C16.77 18.67 16.17 19 15.5 19L4.5 18.99C3.4 18.99 2.5 18.1 2.5 17V7C2.5 5.9 3.4 5.01 4.5 5.01L15.5 5ZM4.5 17H15.5L19.05 12L15.5 7H4.5V17Z" fill="black" fill-opacity="0.6"/>
                                    </svg>
                                {/if}
                                <span>{tag.name}</span>
                            </div>
                        </div>
                    {/each}
                </div>
            </ul>
        </aside>
    </div>
</div>

<style>    
    :global(body.no-scroll) {
        overflow: hidden;
    }
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
        cursor: pointer;
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
        gap: 25px; /* Space between MORE and RSVP buttons */
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
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.6);
        border: none;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .modal-content {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 80%; /* Occupies 80% of the viewport width */
        height: 70%; /* Occupies 70% of the viewport height */
        max-width: 1200px; /* Ensures a maximum width for large screens */
        max-height: 90%; /* Prevents it from overflowing vertically */
        overflow: auto; /* Adds scrollbars if content exceeds height */
        display: flex;
        flex-direction: row;
        overflow: auto;
    }

    .event-details {
        display: flex;
        flex-direction: row;
        gap: 10px; /* Add space between RSVP, Tags, and Favorite */
        flex-wrap: wrap; /* Allow wrapping if space runs out */
    }
    .modal-right {
        flex: 1; /* Allocate 1 part of space to the right section */
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .event-image {
        width: 400px; /* Increase size of the square */
        height: 400px;
        background: gray; /* Default placeholder color */
        border-radius: 8px;
        margin-right: 5rem;
    }
    .modal-left {
        display: flex;
        flex-direction: column;
        flex: 2;
    }
    .modal-left a {
        width: 75%;
        color: gray;
        margin-top: 1rem;
    }

    .modal-footer {
        margin-top: 20px;
        display: flex;
        justify-content: flex-start; /* Align items to the left */
        align-items: center;
        gap: 10px;
    }

    .modal-footer button {
        border: none;
        cursor: pointer;
    }

    .rsvp-popup {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.6);
        border: none;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .rsvp-content {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 50%; 
        height: 56.5%; 
        overflow: auto; /* Adds scrollbars if content exceeds height */
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .rsvp-popup h2 {
        margin-bottom: 1rem;
        font-size: 1.5rem;
    }

    .rsvp-popup p {
        font-size: 0.9rem;
    }

    .rsvp-popup form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    .rsvp-popup input {
        padding: 0.5rem;
        font-size: 1rem;
        border: 1px solid #ddd;
        border-radius: 5px;
        width: 100%;
        background: lightgray;
        outline: none;
        color: black;
    }

    .rsvp-popup .confirmation {
        margin-top: 1rem;
        font-size: 0.9rem;
        color: green;
    }

    /* Mobile styles for screens with width between 320px and 767px in portrait orientation */
@media (max-width: 767px) and (orientation: portrait) {
    .dashboard {
        padding: 1rem;
        gap: 0.5rem;
        padding-top: 4.5rem;
    }

    .search-container {
        padding-bottom: 0.5rem;
        padding-top: 0.5rem;
    }

    .search-bar {
        width: 100%; /* Make search bar take full width */
        height: 40px;
        padding-left: 1.5rem;
    }

    .search-bar svg.mag {
        left: 8px; /* Reduce left padding for the icon */
    }

    .search-bar svg.mic {
        right: 8px; /* Adjust icon placement */
    }

    .content-container {
        flex-direction: column; /* Stack the sidebar and event grid vertically */
    }

    .sidebar {
        width: 100%; /* Make sidebar take full width */
        height: auto; /* Adjust height to content */
        padding: 1rem;
        box-shadow: none;
        margin-bottom: 1rem; /* Add spacing below the sidebar */
    }

    .sidebar-grid {
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); /* Wrap tags dynamically */
        gap: 0.5rem;
    }

    .sidebar h3 {
        margin-left: 0;
        font-size: 18px;
        text-align: center;
    }

   
    .events-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive columns */
        gap: 1rem; 
        justify-content: center; 
        padding: 1rem; 
    }

    .card {
        background: linear-gradient(to bottom, var(--bg-color) 55%, white 50%);
        margin: 0 auto; 
    }

    h3 {
        font-size: 1rem; 
    }

    .creator, p {
        font-size: 12px; /* Adjust text size */
    }

    .buttons {
        flex-direction: row; /* Stack buttons vertically */
        gap: 0.5rem;
    }

    .right-icons {
        gap: 16px; /* Adjust spacing between icons */
    }

    .modal-content {
        width: 95%; /* Reduce modal width */
        height: auto; /* Adjust height for scrolling */
        flex-direction: column; /* Stack modal content vertically */
        padding: 20px;
    }

    .modal-left, .modal-right {
        width: 100%; /* Full width for both sections */
        margin-bottom: 1rem; /* Add spacing */
    }

    .event-image {
        width: 300px; /* Reduce image size */
        height: 300px;
        margin: 0 auto; /* Center the image */
    }

    .modal-footer {
        justify-content: center; /* Center footer content */
    }

    .tag {
        padding: 10px;
        font-size: 12px;
    }

    .search-bar input {
        font-size: 0.9rem; /* Smaller font for input */
    }

    .tag.entertainment-tag span {
        font-size: 11px; /* Smaller font for Entertainment tag */
    }

    .rsvp-content {
        width: 90%; /* Full width for smaller screens */
        height: auto; /* Adjust height to fit content */
        padding: 20px; /* Reduce padding for smaller screens */
    }

    .rsvp-popup h2 {
        font-size: 1.2rem; /* Smaller heading size */
    }

    .rsvp-popup input {
        font-size: 0.9rem; /* Adjust font size for smaller inputs */
    }

    .rsvp-popup p {
        font-size: 0.8rem; /* Smaller paragraph font size */
    }

    .rsvp-popup form {
        gap: 0.8rem; /* Reduce gap between form fields */
    }

    .rsvp-content button {
        font-size: 1rem; /* Ensure buttons remain accessible */
    }
}

</style>
