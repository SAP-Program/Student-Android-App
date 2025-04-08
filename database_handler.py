import mysql.connector

db = mysql.connector.connect(
    host="185.4.28.110",  
    user="root",
    port=5000,   
    password="sapprogram2583",
    database='sap'
)
cursor = db.cursor()

def check_identity(nc, password):
    cursor.execute('SELECT * FROM students WHERE student_national_code=%s', (nc,))
    student = cursor.fetchall()
    if student == [] or student[0][4] != password:
        return False
    else:
        return True

if __name__=='__main__':
    print(check_identity('4712054034', '123'))
