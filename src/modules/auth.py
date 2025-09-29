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

def send_verification_code_to_admin():
    conn = sqlite3.connect("data/campuscore.db")
    cursor = conn.cursor()

    # Get admin's person_id
    cursor.execute("SELECT person_id FROM admin WHERE id = 1")
    row = cursor.fetchone()
    if not row:
        conn.close()
        return None  # No admin found

    person_id = row[0]

    # Get admin's email from contact table
    cursor.execute("""
        SELECT value FROM contact
        WHERE person_id = ? AND type = 'email'
        LIMIT 1
    """, (person_id,))
    email_row = cursor.fetchone()
    conn.close()

    if not email_row:
        return None  # No email found

    admin_email = email_row[0]
    import smtplib, random
    code = str(random.randint(100000, 999999))

    try:
        message = f"Subject: CampusCore Verification\n\nYour verification code is: {code}"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('mshaheerhussain902@gmail.com', 'your_app_password')  # Replace with your actual app password
        server.sendmail('mshaheerhussain902@gmail.com', admin_email, message)
        server.quit()
        return code
    except Exception as e:
        print("❌ Email send failed:", e)
        return None