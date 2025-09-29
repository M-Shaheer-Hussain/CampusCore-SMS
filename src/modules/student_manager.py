import sqlite3
from datetime import date

def add_student(data):
    conn=sqlite3.connect("data/campuscore.db")
    cursor=conn.cursor()

    #insert into person

    cursor.execute('''
                   INSERT INTO person (fathername,mothername,dob,address,gender)
                   VALUES (?,?,?,?,?)
                   ''',(data['fathername'],data['mothername'],data['dob'],data['address'],data['gender']))
    
    person_id=cursor.lastrowid

    #insert into Fullname

    cursor.execute('''INSERT INTO fullname (person_id,first_name,middle_name,last_name)
                   VALUES (?,?,?,?)
                   ''',(person_id,data['first_name'],data['middle_name'],data['last_name'],))
    
    #insert into contact
    #Handling multiple Contacts

    for contact in data['contact']:
        cursor.execute('''INSERT INTO contact (person_id,type,value,label)
                       VALUES (?,?,?,?)
                       ''',(person_id,contact['type'],contact['value'],contact['label']))
        
    #inserting into Student

    cursor.execute('''INSERT INTO student (person_id,date_of_admission,monthly_fee,annual_fund,class)
                   VALUES (?,?,?,?,?)
                   ''',(person_id,data['date_of_admission'],data['monthly_fee'],data['annual_fund'],data['class']))
    
    conn.commit()
    conn.close()
    print("Student Added successfully.")