-- Drop existing tables to reset the database
DROP TABLE IF EXISTS user_event_preferences;
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS organizations;

-- Create the students table
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Create the organizations table
CREATE TABLE organizations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    organization_name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Create the events table
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    created_by TEXT NOT NULL
);

-- Create the user_event_preferences table
CREATE TABLE user_event_preferences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    preference_type TEXT NOT NULL CHECK(preference_type IN ('RSVP', 'Favorite')),
    FOREIGN KEY (user_id) REFERENCES students(id),
    FOREIGN KEY (event_id) REFERENCES events(id)
);

-- Create the notifications table
CREATE TABLE notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    notification_type TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(id)
);

-- Insert sample data into the students table
INSERT INTO students (student_id, email, password)
VALUES ('S12345', 'student1@example.com', 'password123');

-- Insert sample data into the organizations table
INSERT INTO organizations (organization_name, email, password)
VALUES ('Tech Club', 'techclub@example.com', 'securepass');

-- Insert sample data into the events table
INSERT INTO events (name, date, location, description, category, created_by)
VALUES 
('Campus Fair', '2024-11-20', 'Main Campus', 'Annual fair with booths and games', 'Entertainment', 'admin'),
('Tech Workshop', '2024-11-25', 'Room 101', 'Learn Python basics', 'Educational', 'Tech Club');

-- Insert sample data into the user_event_preferences table
INSERT INTO user_event_preferences (user_id, event_id, preference_type)
VALUES 
(1, 1, 'RSVP'),
(1, 2, 'Favorite');

-- Insert sample data into the notifications table
INSERT INTO notifications (event_id, notification_type, message)
VALUES 
(1, 'reminder', 'Reminder: Campus Fair is tomorrow!'),
(2, 'update', 'Tech Workshop: Start time changed to 10:00 AM');
