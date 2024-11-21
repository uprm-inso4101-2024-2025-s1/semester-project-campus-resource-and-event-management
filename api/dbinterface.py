import sqlite3
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Event type constants
EVENT_REMINDER = "reminder"
EVENT_UPDATE = "update"
CANCELLATION = "cancellation"


def connect_db():
    conn = sqlite3.connect('.venv/database.db')  #  database file
    return conn

# Function to create tables if they do not exist
def create_tables():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS organizations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                organization_name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_event_preferences (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                event_id INTEGER NOT NULL,
                preference_type TEXT NOT NULL CHECK(preference_type IN ('RSVP', 'Favorite')),
                FOREIGN KEY (user_id) REFERENCES students(id),
                FOREIGN KEY (event_id) REFERENCES events(id)
            )
        ''')
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            created_by TEXT NOT NULL
        );
    """)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id INTEGER NOT NULL,
                notification_type TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print("Tables created successfully")

    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to insert a new student
def insert_student(student_id, email, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (student_id, email, password) VALUES (?, ?, ?)
        ''', (student_id, email, password))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def get_student_by_id(student_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        student = cursor.fetchone()
        conn.close()
        return student

def update_student(student_id, new_email, new_password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
                UPDATE students SET email = ?, password = ? WHERE student_id = ?
         ''', (new_email, new_password, student_id))
        conn.commit()
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            conn.close()

def delete_student(student_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        conn.commit()
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            conn.close()

# Function to insert a new organization
def insert_organization(organization_name, email, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO organizations (organization_name, email, password) VALUES (?, ?, ?)
    ''', (organization_name, email, password))
        conn.commit()
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            conn.close()

def get_organization_by_name(organization_name):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM organizations WHERE organization_name = ?', (organization_name,))
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            organization = cursor.fetchone()
            conn.close()
            return organization

def update_organization(organization_name, new_email, new_password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE organizations SET email = ?, password = ? WHERE organization_name = ?
    ''', (new_email, new_password, organization_name))
        conn.commit()
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            conn.close()

def delete_organization(organization_name):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM organizations WHERE organization_name = ?', (organization_name,))
        conn.commit()
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            conn.close()

# Function to clear existing tables
def clear_tables():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS students')
        cursor.execute('DROP TABLE IF EXISTS organizations')
        cursor.execute('DROP TABLE IF EXISTS user_event_preferences')
        cursor.execute('DROP TABLE IF EXISTS events')
        conn.commit()
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            conn.close()

# Function to query and display all students
def fetch_students():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        #cursor.execute('SELECT student_id, email, password FROM students')
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            rows = cursor.fetchall()
            conn.close()
            return rows

# Function to query and display all organizations
def fetch_organizations():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM organizations')
        #cursor.execute('SELECT organization_name, email, password FROM organizations')
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            rows = cursor.fetchall()
            conn.close()
            return rows

def add_user_event_preference(user_id, event_id, preference_type):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO user_event_preferences (user_id, event_id, preference_type) 
            VALUES (?, ?, ?)
        ''', (user_id, event_id, preference_type))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Run the server with SocketIO
if __name__ == '__main__':
    socketio.run(app, port=5173,debug=True)