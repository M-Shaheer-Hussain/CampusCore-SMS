import sqlite3

def add_receptionist(data):
    conn = sqlite3.connect("data/campuscore.db")
    cursor = conn.cursor()

    # Insert into person
    cursor.execute('''
        INSERT INTO person (fathername, mothername, dob, address, gender)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['fathername'], data['mothername'], data['dob'], data['address'], data['gender']))
    person_id = cursor.lastrowid

    # Insert into fullname
    cursor.execute('''
        INSERT INTO fullname (person_id, first_name, middle_name, last_name)
        VALUES (?, ?, ?, ?)
    ''', (person_id, data['first_name'], data['middle_name'], data['last_name']))

    # Insert into contact (optional)
    for contact in data.get('contact', []):
        cursor.execute('''
            INSERT INTO contact (person_id, type, value, label)
            VALUES (?, ?, ?, ?)
        ''', (person_id, contact['type'], contact['value'], contact['label']))

    # Insert into receptionist
    cursor.execute('''
        INSERT INTO receptionist (person_id, password)
        VALUES (?, ?)
    ''', (person_id, data['password']))

    conn.commit()
    conn.close()
    print("✅ Receptionist added successfully.")