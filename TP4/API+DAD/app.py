from flask import Flask,jsonify, request 
import repository 

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return "c est top rest !" 

@app.route('/students', methods = ['GET'])
def get_students(): 
    students = repository.get_all_students() 
    return jsonify(students), 200 

@app.route('/students/<int:id>', methods = ['GET'])
def get_student_by_id(id): 
    student = repository.get_student_by_id(id) 
    return jsonify(student), 200 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5001, debug =True)
