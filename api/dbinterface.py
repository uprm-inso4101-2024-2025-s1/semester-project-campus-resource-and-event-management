import sqlite3

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
        conn.commit()
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
        conn.commit()
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
        conn.commit()
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            conn.close()
    
#clear_tables()

# Call this function once to create the tables
create_tables()

# Function to query and display all students
def fetch_students():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        #cursor.execute('SELECT student_id, email, password FROM students')
        conn.commit()
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
        conn.commit()
    except sqlite3.Error as e:
            print(f"An error occurred: {e}")
    finally:
            rows = cursor.fetchall()
            conn.close()
            return rows



