import sqlite3

def verify_receptionist(username, password):
    import sqlite3
    conn = sqlite3.connect("data/campuscore.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT r.password
        FROM receptionist r
        JOIN fullname f ON r.person_id = f.person_id
        WHERE f.first_name = ?
    ''', (username,))
    row = cursor.fetchone()
    conn.close()

    return row and row[0] == password

def verify_admin_password(password):
    import sqlite3
    conn = sqlite3.connect("data/campuscore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM admin WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return row and row[0] == password

def create_receptionist(username, password):
    conn = sqlite3.connect("data/campuscore.db")
    cursor = conn.cursor()
    # Insert into person
    cursor.execute("INSERT INTO person (fathername, mothername, dob, address, gender) VALUES ('', '', '', '', '')")
    person_id = cursor.lastrowid
    # Insert into fullname
    cursor.execute("INSERT INTO fullname (person_id, first_name, middle_name, last_name) VALUES (?, ?, '', '')", (person_id, username))
    # Insert into receptionist
    cursor.execute("INSERT INTO receptionist (person_id, password) VALUES (?, ?)", (person_id, password))
    conn.commit()
    conn.close()
