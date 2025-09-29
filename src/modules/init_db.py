import sqlite3

def initialize_db():

    conn = sqlite3.connect("data/campuscore.db")
    cursor = conn.cursor()

    #Base Person Table
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS person (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fathername TEXT NOT NULL,
                    mothername TEXT NOT NULL,
                    DOB DATE NOT NULL,
                    address TEXT NOT NULL,
                    gender TEXT NOT NULL
                   )
                   ''')

    #FullName Table
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS fullname (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   person_id INTEGER NOT NULL,
                   first_name TEXT NOT NULL,
                   middle_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
                   )
                   ''')
    
    #Contact Info Table
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS contact(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   person_id INTEGER NOT NULL,
                   type TEXT NOT NULL,
                   value TEXT NOT NULL,
                   FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
                   )
                   ''')
    #Student Table
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS student (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   person_id INTEGER NOT NULL,
                   dateOFadmission DATE NOT NULL,
                   monthlyfee DOUBLE,
                   annualFund DOUBLE,
                   class TEXT NOT NULL,
                   FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
                   )
                   ''')
    
    #Teacher Table
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS teacher(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   person_id INTEGER NOT NULL,
                   joiningDate DATE NOT NULL,
                   Salary double NOT NULL,
                   rating INTEGER CHECK(rating BETWEEN 1 AND 5),
                   FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
                   )
                   ''')
    
    #Admin
    cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   person_id INTEGER NOT NULL,
                   FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
                   )
                   ''')
    #Receptionist
    cursor.execute('''CREATE TABLE IF NOT EXISTS receptionist(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   person_id INTEGER NOT NULL,
                   FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
                   )
                   ''')
    conn.commit()
    conn.close()