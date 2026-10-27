import sqlite3
import pandas as pd

DB_NAME = "hris.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS staff_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dob TEXT,
            age INTEGER,
            father_name TEXT,
            mother_name TEXT,
            nationality TEXT,
            ethnicity TEXT,
            religion TEXT,
            blood_type TEXT,
            marital_status TEXT,
            spouse_name TEXT,
            enrollment_date TEXT,
            hearing TEXT,
            seeing TEXT,
            health_remark TEXT,
            curr_org TEXT,
            curr_pos TEXT,
            duty_station TEXT,
            salary REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_staff_profile(data: dict):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO staff_profiles 
        (name, dob, age, father_name, mother_name, nationality, ethnicity, religion, 
         blood_type, marital_status, spouse_name, enrollment_date, hearing, seeing, 
         health_remark, curr_org, curr_pos, duty_station, salary)
        VALUES (:name, :dob, :age, :father_name, :mother_name, :nationality, :ethnicity, :religion,
                :blood_type, :marital_status, :spouse_name, :enrollment_date, :hearing, :seeing,
                :health_remark, :curr_org, :curr_pos, :duty_station, :salary)
    ''', data)
    conn.commit()
    conn.close()

def update_staff_profile(profile_id: int, data: dict):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        UPDATE staff_profiles
        SET name=:name, dob=:dob, age=:age, father_name=:father_name, mother_name=:mother_name,
            nationality=:nationality, ethnicity=:ethnicity, religion=:religion, blood_type=:blood_type,
            marital_status=:marital_status, spouse_name=:spouse_name, enrollment_date=:enrollment_date,
            hearing=:hearing, seeing=:seeing, health_remark=:health_remark, curr_org=:curr_org,
            curr_pos=:curr_pos, duty_station=:duty_station, salary=:salary
        WHERE id = :id
    ''', {**data, "id": profile_id})
    conn.commit()
    conn.close()

def delete_staff_profile(profile_id: int):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM staff_profiles WHERE id = ?", (profile_id,))
    conn.commit()
    conn.close()

def get_all_profiles():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM staff_profiles ORDER BY id DESC", conn)
    conn.close()
    return df