<script>
    import saveIcon from "../assets/diskette.png";
    import attendeesIcon from "../assets/add-group.png";
    import clockIcon from "../assets/clock.png";
    import locationIcon from "../assets/location.png";
    import refreshIcon from "../assets/refresh.png";
    import videoIcon from "../assets/video-camera.png";
    import texteraIcon from "../assets/justify-paragraph.png";
</script>

<style> 

    .container {
        width: 90%; 
        max-width: 800px;
        background-color: #0C9D7A; 
        border: 2px solid white;
        border-radius: 8px; 
        padding: 20px; 
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.2); 
    }
    .save-section {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 15px;
        border-bottom: 1px solid #444;
        margin-bottom: 15px;
    }

    .save-section button {
        display: flex;
        align-items: center;
        background-color: blue;
        border: none;
        border-radius: 4px;
        padding: 10px 15px;
        color: white;
        font-size: 14px;
        cursor: pointer;
    }

    .save-section button img {
        width: 20px;
        height: 20px;
        margin-right: 8px;
    }

    .save-section .calendar-info {
        font-size: 14px;
        color: white;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .line-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #0C9D7A;
        border: 1px solid #444;
        border-radius: 4px;
        padding: 10px 15px;
        color: white;
        gap: 10px;
    }

    .left-section {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .left-section img {
        width: 24px;
        height: 24px;
    }

    .left-section input {
        background: transparent;
        border: none;
        outline: none;
        color: white;
        font-size: 16px;
        flex-grow: 1;
    }

    .right-section {
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .right-section label {
        font-size: 14px;
    }

    .right-section input[type="checkbox"] {
        width: 16px;
        height: 16px;
    }
    .attendees-line-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #0C9D7A;
        border: none;
        border-bottom: 1px solid #444;
        padding: 10px 15px;
        color: white;
        gap: 10px;
    }

    .attendees-left-section {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .attendees-left-section img {
        width: 20px;
        height: 20px;
    }

    .attendees-left-section label {
        font-size: 14px;
        color: white;
        cursor: pointer;
    }

    .attendees-right-section {
        font-size: 14px;
        color: blue; 
        cursor: pointer;
    }

    .datetime-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #0C9D7A;
        border: none;
        border-bottom: 1px solid #444;
        padding: 10px 15px;
        gap: 10px;
    }

    .datetime-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .datetime-left img {
        width: 20px;
        height: 20px;
    }

    .datetime-left input {
        padding: 8px;
        border: 1px solid #444;
        border-radius: 4px;
        background-color: #0C9D7A;
        color: white;
        font-size: 14px;
        width: 120px;
    }

    .datetime-left select {
        padding: 8px;
        border: 1px solid #444;
        border-radius: 4px;
        background-color: #0C9D7A;
        color: white;
        font-size: 14px;
        width: 100px;
    }

    .datetime-right {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .datetime-right img {
        width: 20px;
        height: 20px;
    }

    .datetime-right label {
        font-size: 14px;
        color: blue;
        cursor: pointer;
    }

    .datetime-right input[type="checkbox"] {
        width: 16px;
        height: 16px;
        cursor: pointer;
    }

    .location-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #0C9D7A;
        border: none;
        border-bottom: 1px solid #444;
        padding: 10px 15px;
        color: white;
        gap: 10px;
    }

    .location-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .location-left img {
        width: 20px;
        height: 20px;
    }

    .location-left label {
        font-size: 14px;
        color: white;
    }

    .location-right {
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .location-right input[type="checkbox"] {
        width: 16px;
        height: 16px;
        cursor: pointer;
    }

    .location-right label {
        font-size: 14px;
        color: white;
        cursor: pointer;
    }

    .text-area-container {
        display: flex;
        align-items: flex-start;
        background-color: #0C9D7A;
        border: 1px solid #444;
        border-radius: 4px;
        padding: 10px 15px;
        color: white;
        gap: 10px;
    }

    .text-area-icon {
        display: flex;
        align-items: center;
        margin-top: 5px;
    }

    .text-area-icon img {
        width: 16px;
        height: 16px;
    }

    .text-area {
        flex-grow: 1;
        border: none;
        outline: none;
        background-color: transparent;
        color: white;
        font-size: 14px;
        font-family: Arial, sans-serif;
        resize: none; 
        height: 100px;
    }

    .text-area::placeholder {
        color: #aaa;
    }
</style>


<body>
<div class="container">

    <!-- Save Section -->
    <div class="save-section">
        <button>
            <img src={saveIcon} alt="Save Icon">
            Save
        </button>
        <div class="calendar-info">
            <span>●</span> Calendar (assadasdasdaxas)
        </div>
    </div>

    <div class="line-container">
        <!-- Left Section -->
        <div class="left-section">
            <img src={"addGroupIcon"} alt="Add Group Icon">
            <input type="text" placeholder="Add a title" />
        </div>
    
        <!-- Right Section -->
        <div class="right-section">
            <input type="checkbox" id="teams-meeting" />
            <label for="teams-meeting">
                <img src={videoIcon} alt="Teams Meeting Icon" style="width: 16px; height: 16px; margin-right: 5px;">
                Teams meeting
            </label>
        </div>
    </div>

    <div class="attendees-line-container">
        <!-- Sección Izquierda -->
        <div class="attendees-left-section">
            <img src={attendeesIcon} alt="Invite Icon">
            <label for="attendees-input">Invite attendees</label>
        </div>
    
        <!-- Sección Derecha -->
        <div class="attendees-right-section">
            Optional
        </div>
    </div>

    <div class="datetime-container">
        <!-- Sección Izquierda -->
        <div class="datetime-left">
            <img src={clockIcon} alt="Clock Icon">
            <input type="date" value="2024-10-11">
            <input type="time" value="16:00">
            <span>to</span>
            <input type="time" value="16:30">
        </div>
    
        <div class="datetime-right">
            <!-- <img src={globeIcon} alt="Globe Icon"> -->
            
            <!-- Asocia el label con un input oculto -->
            <input type="checkbox" id="make-recurring" style="display: none;">
            <label for="make-recurring">
                <img src={refreshIcon} alt="Refresh Icon" style="margin-right: 5px;">
                Make recurring
            </label>
        
            <!-- Checkbox para "All day" -->
            <label>
                <input type="checkbox">
                All day
            </label>
        </div>
    </div>

    <div class="location-container">
        <!-- Sección Izquierda -->
        <div class="location-left">
            <img src={locationIcon} alt="Location Icon">
            <label for="room-location">Search for a room or location</label>
        </div>
    
        <!-- Sección Derecha -->
        <div class="location-right">
            <input type="checkbox" id="in-person-event">
            <label for="in-person-event">In-person event</label>
        </div>
    </div>

    <div class="text-area-container">
        <!-- Ícono -->
        <div class="text-area-icon">
            <img src={texteraIcon} alt="Menu Icon">
        </div>
    
        <!-- Área de texto -->
        <textarea 
            class="text-area" 
            placeholder="Type / to insert files and more">
        </textarea>
    </div>
</div>
</body>
