from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from src.service import createChallenge, updateChallenge, deleteChallenge

challenges = Blueprint("challenges", __name__)

@challenges.route("/api/add-challenge", methods=["POST"])
@login_required
def create_challenge():
    titulo = request.form.get("titulo")
    descripcion = request.form.get("descripcion")
    tema = request.form.get("topic")
    dificultad = request.form.get("dificultad")
    id = current_user.usuario_Id
    try:
        challenge = createChallenge(titulo=titulo, descripcion=descripcion, dificultad=dificultad, tema=tema, usuario_Id=id)
        if not challenge:
            return jsonify({"message": "No se creo el reto.", "status": 400}), 400
        return jsonify({"message": "Reto creado", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal", "status": 500, "error": str(e)}), 500
    
@challenges.route("/api/update-challenge/<int:id>", methods=["PUT"])
@login_required
def update_challenge(id):
    data = request.form.to_dict()
    try:
        challenge = updateChallenge(id=id, data=data)
        if not challenge:
            return jsonify({"message": "No se ha actualizado el reto", "status": 400}), 400
        return jsonify({"message": "Reto actualizado correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})
    
@challenges.route("/api/delete-challenge/<int:id>", methods=["DELETE"])
@login_required
def delete_challenge(id):
    try:
        challenge = deleteChallenge(id=id)
        if not challenge:
            return jsonify({"message": "No se ha eliminado el reto", "status": 400}), 400
        return jsonify({"message": "Reto eliminado correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})
