import sqlite3

def connect_db():
    conn = sqlite3.connect('.venv/Test_database.db')  #  database file
    return conn

# Function to create tables if they do not exist
def create_tables():
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
    conn.commit()
    conn.close()

# Function to insert a new student
def insert_student(student_id, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (student_id, email, password) VALUES (?, ?, ?)
    ''', (student_id, email, password))
    conn.commit()
    conn.close()

# Function to insert a new organization
def insert_organization(organization_name, email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO organizations (organization_name, email, password) VALUES (?, ?, ?)
    ''', (organization_name, email, password))
    conn.commit()
    conn.close()




# Function to clear existing tables
def clear_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS students')
    cursor.execute('DROP TABLE IF EXISTS organizations')
    conn.commit()
    conn.close()
    
#clear_tables()

# Call this function once to create the tables
create_tables()

# Function to query and display all students
def fetch_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    #cursor.execute('SELECT student_id, email, password FROM students')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to query and display all organizations
def fetch_organizations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM organizations')
    #cursor.execute('SELECT organization_name, email, password FROM organizations')
    rows = cursor.fetchall()
    conn.close()
    return rows

# if __name__ == "__main__":
#     # Fetch and display students
#     students = fetch_students()
#     print("Students:")
#     for student in students:
#         print(student)

#     # Fetch and display organizations
#     organizations = fetch_organizations()
#     print("\nOrganizations:")
#     for organization in organizations:
#         print(organization)


