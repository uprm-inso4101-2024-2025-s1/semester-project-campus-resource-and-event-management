import requests

#GET ALL EVENTS TEST
response = requests.get("http://localhost:5173/api/events")
if response.status_code == 200:
    print("Events fetched successfully:")
    print(response.json())
else:
    print("Error fetching events:", response.json())


#CREATE EVENT TEST
data = {
    "name": "New Event",
    "date": "2024-12-05",
    "location": "Library",
    "description": "A special event",
    "category": "Entertainment",
    "created_by": "user123"
}

response = requests.post("http://localhost:5173/api/events", json=data)
# Print the raw content to see what's returned from the server

if response.status_code == 201:
    print("Event created successfully:")
    print(response.json())
else:
    print("Error creating event:", response.text)  # Print the response text instead of JSON

#UPDATE EVENT TEST
url = "http://localhost:5173/api/events/1"  # Replace with the actual event ID you want to update

updated_event_data = {
    "name": "Updated Event Name",
    "date": "2024-12-10",
    "location": "Updated Location",
    "description": "Updated description",
    "category": "Updated category",
    "created_by": "admin"
}

response = requests.put(url, json=updated_event_data)

if response.status_code == 200:
    print("Event updated successfully:")
    print(response.json())
else:
    print(f"Error updating event. Status code: {response.status_code}")
    print("Response Text:", response.text)

#DELETE EVENT TEST
url = "http://localhost:5173/api/events/1"  # Replace with the actual event ID you want to delete

response = requests.delete(url)

if response.status_code == 200:
    print("Event deleted successfully:")
    print(response.json())
else:
    print(f"Error deleting event. Status code: {response.status_code}")
    print("Response Text:", response.text)

