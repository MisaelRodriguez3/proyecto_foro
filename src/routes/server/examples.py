from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from src.service import createExample, updateExample, deleteExample

examples = Blueprint("examples", __name__)

@examples.route("/api/add-example", methods=["POST"])
@login_required
def create_example():
    titulo = request.form.get("titulo")
    descripcion = request.form.get("descripcion")
    codigo = request.form.get("codigo")
    topic = request.form.get("topic")
    user_Id = current_user.usuario_Id

    try:
        example = createExample(titulo=titulo, descripcion=descripcion, codigo=codigo, tema=topic, usuario_Id=user_Id)
        if not example:
            return jsonify({"message": "No se ha creado el ejemplo", "status": 400}), 400
        return jsonify({"message": "Ejemplo creado correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})
    
@examples.route("/api/update-example/<int:id>", methods=["PUT"])
@login_required
def update_example(id):
    data = request.form.to_dict()

    try:
        example = updateExample(id=id, data=data)
        if not example:
            return jsonify({"message": "No se ha actualizado el ejemplo", "status": 400}), 400
        return jsonify({"message": "Ejemplo actualizado correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})        
    
@examples.route("/api/delete-example/<int:id>", methods=["DELETE"])
@login_required
def delete_example(id):
    try:
        example = deleteExample(id=id)
        if not example:
            return jsonify({"message": "No se ha eliminado el ejemplo", "status": 400}), 400
        return jsonify({"message": "Ejemplo eliminado correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})