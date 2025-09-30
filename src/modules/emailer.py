import sqlite3
import smtplib
import random

def send_verification_code(reason_for:str):
    conn = sqlite3.connect("data/campuscore.db")
    cursor = conn.cursor()

    # Get admin's person_id
    cursor.execute("SELECT person_id FROM admin WHERE id = 1")
    row = cursor.fetchone()
    if not row:
        conn.close()
        return None  # No admin exists

    person_id = row[0]
    print(person_id)

    # Get admin's email from contact table
    cursor.execute("""
        SELECT value FROM contact
        WHERE person_id = ? AND type = 'email'
        LIMIT 1
    """, (person_id,))
    email_row = cursor.fetchone()
    conn.close()

    if not email_row:
        return None  # No email found, skip email verification

    admin_email = email_row[0]
    code = str(random.randint(100000, 999999))

    try:
        message = f"Subject: CampusCore Verification\n\nYour verification code {reason_for}is: {code}"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('mshaheerhussain902@gmail.com', 'asov uziu frfo zkzn')
        server.sendmail('mshaheerhussain902@gmail.com', admin_email, message)
        server.quit()
        return code
    except Exception as e:
        print("❌ Email send failed:", e)
        return None