import sqlite3

conn = sqlite3.connect("hris.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL
)
''')

# Define all required Excel columns
required_columns = {
    "dob": "TEXT",
    "age": "INTEGER",
    "father_name": "TEXT",
    "mother_name": "TEXT",
    "nationality": "TEXT",
    "ethnicity": "TEXT",
    "religion": "TEXT",
    "blood_type": "TEXT",
    "marital_status": "TEXT",
    "spouse_name": "TEXT",
    "enrollment_date": "TEXT",
    "hearing_status": "TEXT",
    "seeing_status": "TEXT",
    "id_type": "TEXT",
    "present_address": "TEXT",
    "permanent_address": "TEXT",
    "parent_address": "TEXT",
    "emergency_contact_name": "TEXT",
    "emergency_contact_relation": "TEXT",
    "emergency_contact_phone": "TEXT",
    "emergency_contact_email": "TEXT",
    "emergency_contact_address": "TEXT",
    "dependents_count": "INTEGER",
    "interests": "TEXT",
    "hobbies": "TEXT",
    "further_info": "TEXT"
}

# Fetch current columns in employees table
cursor.execute("PRAGMA table_info(employees)")
existing_columns = [row[1] for row in cursor.fetchall()]

# Safely add any missing columns
for col_name, col_type in required_columns.items():
    if col_name not in existing_columns:
        cursor.execute(f"ALTER TABLE employees ADD COLUMN {col_name} {col_type}")

# Create secondary tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS leave_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    leave_type TEXT,
    start_date TEXT,
    end_date TEXT,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY(employee_id) REFERENCES employees(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_name TEXT NOT NULL,
    serial_number TEXT UNIQUE,
    assigned_to INTEGER,
    status TEXT DEFAULT 'Assigned',
    FOREIGN KEY(assigned_to) REFERENCES employees(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS procurement (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requested_by INTEGER,
    item_description TEXT NOT NULL,
    estimated_cost REAL,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY(requested_by) REFERENCES employees(id)
)
''')

conn.commit()
conn.close()
print("Successfully migrated database schema! All missing columns added.")