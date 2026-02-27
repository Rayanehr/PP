from db import get_connection 

def get_all_students(): 
    conn = get_connection() 
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * from students")
    result = cursor.fetchall()
    cursor.close() 
    conn.close()
    return result 

def get_student_by_id(id): 
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query= ("Select * from students WHERE id = %s")
    cursor.execute(query, (id,))
    student = cursor.fetchall()
    cursor.close()
    conn.close()
    return student 
