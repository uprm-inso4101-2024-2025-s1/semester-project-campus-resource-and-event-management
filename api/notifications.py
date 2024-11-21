from apscheduler.schedulers.background import BackgroundScheduler
from flask_socketio import SocketIO, emit
import socketio
from dbinterface import connect_db, EVENT_REMINDER, EVENT_UPDATE, CANCELLATION
import sqlite3



scheduler = BackgroundScheduler()
scheduler.start()

# Event trigger for a new notification
def trigger_notification(event_id, notification_type, message):
    # Emit notification to all connected clients
    socketio.emit('notification', {
        'event_id': event_id,
        'type': notification_type,
        'message': message
    })

def add_notification(event_id, notification_type, message):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO notifications (event_id, notification_type, message)
            VALUES (?, ?, ?)
        ''', (event_id, notification_type, message))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def send_event_reminder_notifications():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Fetch upcoming events and users who have RSVP’d or favorited
        cursor.execute('''
            SELECT user_id, event_id
            FROM user_event_preferences
            WHERE preference_type IN ('RSVP', 'Favorite')
        ''')
        
        for user_id, event_id in cursor.fetchall():
            # Placeholder: send_notification(user_id, f"Reminder for your upcoming event with ID {event_id}!")
            print(f"Sending reminder to user {user_id} for event {event_id}")
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def cancel_event(event_id):
    # Delete the event or mark it as canceled
    add_notification(event_id, CANCELLATION, "The event has been canceled.")
    trigger_notification(event_id, CANCELLATION, "The event has been canceled.")

def update_event(event_id, new_details):
    # Update event in database
    add_notification(event_id, EVENT_UPDATE, "The event details have been updated.")
    trigger_notification(event_id, EVENT_UPDATE, "The event details have been updated.")

def schedule_reminder(event_id):
    # Use a scheduler to trigger at the appropriate time
    scheduler.add_job(
        func=lambda: trigger_notification(event_id, EVENT_REMINDER, "Reminder for your event!"),
        trigger='date',
        run_date='2024-01-01 12:00:00'
    )
    add_notification(event_id, EVENT_REMINDER, "Reminder: Your event is coming up soon!")
    trigger_notification(event_id, EVENT_REMINDER, "Reminder: Your event is coming up soon!")

# Broadcast notifications
def broadcast_notification(socketio,message):
    socketio.emit("notification", {"message": message}, room='/')

# Notification functions
def send_event_update(socketio, event_id):
    message = f"Event {event_id} has been updated!"
    broadcast_notification(socketio, message)

def send_event_cancellation(socketio, event_id):
    message = f"Event {event_id} has been canceled."
    broadcast_notification(socketio, message)

def send_event_reminder(socketio, event_id):
    message = f"Reminder: Event {socketio, event_id} is happening soon!"
    broadcast_notification(message)
