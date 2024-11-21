from flask import Flask, make_response, request, jsonify
from flask_socketio import SocketIO, emit
import sqlite3
from notifications import send_event_update, send_event_cancellation, send_event_reminder, broadcast_notification
from dbinterface import connect_db, create_tables, clear_tables

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")
#HASHHD
connected_clients = []

class reqCounter():
    def __init__(self):
        self.count = 0
    
    def getCount(self):
        self.count += 1
        return self.count
    
reqCount = reqCounter()

@app.route("/api/")
def hello_world():
    resp = make_response(f"This is the server request # {reqCount.getCount()}", 200)

    # Setting CORS request headers
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

# WebSocket connection handler
@socketio.on("connect")
def handle_connect():
    print("Client connected")
    connected_clients.append(request.sid)

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")
    connected_clients.remove(request.sid)

@app.route("/")
def index():
    return "WebSocket Server is Running!"

@socketio.on("message", namespace="/notifications")
def handle_message(msg):
    print("Message received:", msg)
    socketio.emit("response", {"reply": "Message processed"}, namespace="/notifications")

@socketio.on('test_message')
def handle_test_message(msg):
    print(f"Server received: {msg}")
    socketio.emit('test_response', {'message': 'Hello from server!'})

# Broadcast notifications
def broadcast_notification(message):
    socketio.emit("notification", {"message": message}, room='/')

@app.route("/api/trigger_update/<int:event_id>", methods=["GET"])
def trigger_update(event_id):
    send_event_update(socketio, event_id)
    return jsonify({"message": f"Update notification sent for event {event_id}"}), 200

@app.route("/api/trigger_cancellation/<int:event_id>", methods=["GET"])
def trigger_cancellation(event_id):
    send_event_cancellation(socketio, event_id)
    return jsonify({"message": f"Cancellation notification sent for event {event_id}"}), 200

@app.route("/api/trigger_reminder/<int:event_id>", methods=["GET"])
def trigger_reminder(event_id):
    send_event_reminder(socketio, event_id)
    return jsonify({"message": f"Reminder notification sent for event {event_id}"}), 200

# Fetch all events
@app.route('/api/events', methods=['GET'])
def fetch_all_events():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT id, name, date, location, description, category, created_by FROM events"
        cursor.execute(query)
        events = cursor.fetchall()

        # Convert rows to a list of dictionaries
        event_list = [
            {
                "id": row[0],
                "name": row[1],
                "date": row[2],
                "location": row[3],
                "description": row[4],
                "category": row[5],
                "created_by": row[6]
            }
            for row in events
        ]

        conn.close()
        return jsonify(event_list), 200

    except Exception as e:
        return jsonify({"error": "Unable to fetch events", "details": str(e)}), 500

# Create a new event
@app.route('/api/events', methods=['POST'])
def create_event():
    try:
        # Get data from the request
        event_data = request.get_json()

        # Ensure all required fields are present
        if not event_data or not all(key in event_data for key in ["name", "date", "location", "description", "category", "created_by"]):
            return jsonify({"error": "Missing required fields"}), 400

        # Connect to the database and create a new event
        conn = connect_db()
        cursor = conn.cursor()
        query = """
        INSERT INTO events (name, date, location, description, category, created_by)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            event_data['name'],
            event_data['date'],
            event_data['location'],
            event_data['description'],
            event_data['category'],
            event_data['created_by']
        ))
        conn.commit()

        # Fetch the newly created event to return
        cursor.execute("SELECT id, name, date, location, description, category, created_by FROM events WHERE id = ?", (cursor.lastrowid,))
        new_event = cursor.fetchone()

        conn.close()

        # Convert the row to a dictionary
        event_dict = {
            "id": new_event[0],
            "name": new_event[1],
            "date": new_event[2],
            "location": new_event[3],
            "description": new_event[4],
            "category": new_event[5],
            "created_by": new_event[6]
        }

        return jsonify(event_dict), 201  # Return the newly created event

    except Exception as e:
        return jsonify({"error": "Unable to create event", "details": str(e)}), 500

# Update an existing event
@app.route('/api/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    try:
        event_data = request.get_json()

        name = event_data.get('name')
        date = event_data.get('date')
        location = event_data.get('location')
        description = event_data.get('description')
        category = event_data.get('category')
        created_by = event_data.get('created_by')

        conn = connect_db()
        cursor = conn.cursor()

        query = '''
            UPDATE events
            SET name = ?, date = ?, location = ?, description = ?, category = ?, created_by = ?
            WHERE id = ?
        '''
        cursor.execute(query, (name, date, location, description, category, created_by, event_id))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Event not found"}), 404

        conn.close()

        return jsonify({
            "id": event_id,
            "name": name,
            "date": date,
            "location": location,
            "description": description,
            "category": category,
            "created_by": created_by
        }), 200

    except Exception as e:
        return jsonify({"error": "Unable to update event", "details": str(e)}), 500

# Delete an event
@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Delete the event
        query = "DELETE FROM events WHERE id = ?"
        cursor.execute(query, (event_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Event not found"}), 404

        conn.close()

        return jsonify({"message": "Event deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": "Unable to delete event", "details": str(e)}), 500


# Run Flask server with SocketIO
if __name__ == "__main__":
    create_tables()
    socketio.run(app, port=5173)