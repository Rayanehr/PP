from flask import Flask, jsonify, request
app = Flask(__name__)

students = [
    {"id":1,"name":"Youcef", "age":21},
    {"id":2,"name":"Samir", "age":41},
]
@app.route('/')
def home():
    return"Bienvenue dans l'Api de gestion des etudiants !"

#Endpoint pouir listere tous les etudiants 
@app.route('/students',methods=['GET'])
#HTTP 
def get_students(): 
    #jsonif transforme la liste students en json"
    return jsonify(students)
@app.route('/students', methods=['POST'])
def add_student(): 
    new_student=request.get_json()
#Pour recuperer les données envoyé par le client 
    new_student['id']=len(students)+1
#Attribuer un numero de maniere incrementable 
    students.append(new_student)
    return jsonify(new_student),201 #le code 201 pour dire creation reussie 

#afficher un etudiant sachant son identifiant 
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id): 
    student = next((s for s in students if s['id']==id),None)
    if student:
        return jsonify(student)
    return jsonify({"erreur":"l'etudiant n'existe pas!"}),404
#Mettre un jour un etudiant PUT 
@app.route('/students/<int:id>',methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s['id']==id),None)
    if not student:
        return jsonify({"erreur":"l'etudiant n'existe pas!"}),404
    data = request.get_json()
    student.update(data)
    return jsonify(student)

#Supprimer un etudiant 
@app.route('/students/<int:id>',methods=['DELETE'])
def delete_student(id):
    student = next((s for s in students if s['id']==id),None)
    if not student:
        return jsonify({"erreur":"l'etudiant n'existe pas!"}),404
    students.remove(student)
    return jsonify({"message": "Étudiant supprimé"}), 200
if __name__== '__main__':
    app.run(debug=True)