import sqlite3

def initialize_db():
    conn = sqlite3.connect("data/campuscore.db")
    cursor = conn.cursor()

    # Base Person Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fathername TEXT NOT NULL,
            mothername TEXT NOT NULL,
            dob DATE NOT NULL,
            address TEXT NOT NULL,
            gender TEXT NOT NULL
        )
    ''')

    # FullName Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fullname (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
        )
    ''')

    # Contact Info Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            value TEXT NOT NULL,
            label TEXT,
            FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
        )
    ''')

    # Student Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            date_of_admission DATE,
            monthly_fee DOUBLE,
            annual_fund DOUBLE,
            class TEXT NOT NULL,
            FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
        )
    ''')

    # Teacher Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teacher (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            joining_date DATE,
            salary DOUBLE NOT NULL,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
        )
    ''')

    # Admin Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
        )
    ''')

    # Receptionist Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS receptionist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
        )
    ''')

    # Pending Due Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pending_due (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            due_type TEXT NOT NULL,
            amount_due DOUBLE NOT NULL,
            due_date DATE NOT NULL,
            status TEXT DEFAULT 'unpaid',
            FOREIGN KEY(student_id) REFERENCES student(id) ON DELETE CASCADE
        )
    ''')

    # Payment Record Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payment_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pending_due_id INTEGER NOT NULL,
            amount_paid DOUBLE NOT NULL,
            payment_date DATE NOT NULL,
            payment_mode TEXT,
            FOREIGN KEY(pending_due_id) REFERENCES pending_due(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()