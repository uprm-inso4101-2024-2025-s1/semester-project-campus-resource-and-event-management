import socketio

# Create a Socket.IO client
sio = socketio.Client()

# Event handler for connection
@sio.event
def connect():
    print("Connected to the server")
    sio.emit('test_message', {'message': 'Hello from client!'})
    print("Message sent to the server")

# Event handler for disconnection
@sio.event
def disconnect():
    print("Disconnected from the server")

# Event handler for custom notifications
@sio.on("notification")
def handle_notification(data):
    print("Notification received:", data)

@sio.on('test_response')
def handle_response(data):
    print(f"Response from server: {data}")

# Connect to the server
url = "http://localhost:5173"
sio.connect(url)

# Keep the client running to listen for events
sio.wait()