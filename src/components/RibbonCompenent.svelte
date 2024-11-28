<script>
    export let mainCalendarView = 'month';
    import calendar_Img from "../assets/calendar.png";
    
    // Modal visibility state
    let isModalOpen = false;

    // Function to close the modal
    function closeModal() {
        isModalOpen = false;
    }
</script>

<div class="Menu_bar">
    <button 
        class="create_event" 
        on:click={() => (isModalOpen = true)}
    >
        CREATE EVENT
    </button>
    <button 
        on:click={() => mainCalendarView = 'day'} 
        class:currentView={mainCalendarView == 'day'}
    >
        Day
    </button>
    <button 
        on:click={() => mainCalendarView = 'week'} 
        class:currentView={mainCalendarView == 'week'}
    >
        Week
    </button>
    <button 
        on:click={() => mainCalendarView = 'month'} 
        class:currentView={mainCalendarView == 'month'} 
        class="Calendar_Selection"
    >
        Month
    </button>

    <div class="icon_container">
        <img src={calendar_Img} alt="Calendar Icon" class="icon_image">
    </div>
</div>

<!-- Modal -->
{#if isModalOpen}
    <div class="modal-overlay" on:click={closeModal}>
        <div class="modal-content" on:click|stopPropagation>
            <h2>Create Event</h2>
            <form>
                <div>
                    <label for="event-title">Title:</label>
                    <input type="text" id="event-title" placeholder="Event Title" />
                </div>
                <div>
                    <label for="event-date">Date:</label>
                    <input type="date" id="event-date" />
                </div>
                <div>
                    <label for="event-time">Time:</label>
                    <input type="time" id="event-time" />
                </div>
                <div>
                    <label for="event-desc">Description:</label>
                    <textarea id="event-desc" placeholder="Event Description"></textarea>
                </div>
                <div class="modal-buttons">
                    <button type="button" on:click={closeModal} class="cancel-button">Cancel</button>
                    <button type="submit" class="create-button">Create</button>
                </div>
            </form>
        </div>
    </div>
{/if}

<style>
    .Menu_bar {
        background-color: white;
        position: relative;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        border-radius: 1.2em;
        gap: 34px;
    }

    .create_event {
        color: rgb(8, 94, 73);
        position: absolute;
        border-radius: 30px;
        border-color: rgb(8, 94, 73);
        border-style: solid;
        padding: 0 8px;
        height: 80%;
        box-sizing: border-box;
        display: flex;
        font-size: small;
        align-items: center;
        transition: 0.2s;
        left: 0.5em;
    }

    .create_event:hover {
        background-color: rgb(8, 94, 73);
        color: white;
    }

    .icon_container {
        height: 100%;
    }

    .Menu_bar img {
        height: 100%;
    }

    button {
        all: unset;
        font-weight: bolder;
        user-select: none;
        cursor: pointer;
        color: black;
    }

    .currentView, button:hover {
        color: rgb(8, 94, 73);
    }

    /* Modal styles */
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
    }

    .modal-content {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        width: 400px;
        max-width: 90%;
    }

    .modal-content h2 {
        margin-top: 0;
        font-size: 1.5em;
        margin-bottom: 1em;
    }

    .modal-content form {
        display: flex;
        flex-direction: column;
        gap: 1em;
    }

    .modal-content input, .modal-content textarea {
        width: 100%;
        padding: 0.5em;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    .modal-buttons {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
    }

    .cancel-button, .create-button {
        all: unset;
        padding: 0.5em 1em;
        border-radius: 4px;
        cursor: pointer;
    }

    .cancel-button {
        background-color: #f5f5f5;
        color: #333;
    }

    .cancel-button:hover {
        background-color: #e5e5e5;
    }

    .create-button {
        background-color: rgb(8, 94, 73);
        color: white;
    }

    .create-button:hover {
        background-color: rgb(6, 75, 58);
    }
</style>
