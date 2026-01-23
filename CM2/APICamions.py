from flask import Flask, request, jsonify

app = Flask(__name__)

camions = [ 
    {"id":1, "Imma":12345, "annee":2002, "nom" :"VOLVO"},
    {"id":2, "Imma":12347, "annee":2026, "nom" :"DAIWO"},
]

@app.route('/')
def home(): 
    return "Bienvenue dans mon application de camions"

#Afficher tous les camions 
@app.route('/camions') 
def Afficher_camions(): 
    return jsonify(camions)
#Ajouter un camion
@app.route('/camions',methods=['POST'])
def ajouter_camions(): 
    new_camion = request.get_json() 
    camions.append(new_camion)
    return jsonify(new_camion),201 #le code 201 pour dire creation reussie 


#afficher un etudiant sachant son identifiant 
@app.route('/camions/<int:id>', methods=['GET'])
def get_camion(id): 
    camion = next((s for s in camions if s['id']==id),None)
    if camion:
        return jsonify(camion)
    return jsonify({"erreur":"le camion n'existe pas!"}),404



#Mettre un jour un etudiant PUT 
@app.route('/camions/<int:id>',methods=['PUT'])
def update_camion(id):
    camion = next((s for s in camions if s['id']==id),None)
    if not camion:
        return jsonify({"erreur":"le camion n'existe pas!"}),404
    data = request.get_json()
    camion.update(data)
    return jsonify(camion)




#Supprimer un etudiant 
@app.route('/camions/<int:id>',methods=['DELETE'])
def delete_camion(id):
    camion = next((c for c in camions if s['id']==id),None)
    if not camion:
        return jsonify({"erreur":"le camion n'existe pas!"}),404
    camions.remove(camion)
    return jsonify({"message": "camion supprimé"}), 200

#Avoir le nombre de camions par GET
@app.route('/camions/count',methods=['GET']) 
def get_count():
    return jsonify({"Le nombre de camions est : ":len(camions)})

#Récuperer le nombre de camions par année avec get 
@app.route('/camions/count/<int:annee>', methods=['GET'])
def get_count_annee(annee): 
    total = sum(1 for camion in camions if camion['annee'] == annee)
    return jsonify({"annee": annee, "total_camions": total})    

if __name__== '__main__':
    app.run(debug=True)