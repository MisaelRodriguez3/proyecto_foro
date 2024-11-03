from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from src.service import createComment, updateComment, deleteComment

comments = Blueprint("comments", __name__)

@comments.route("/api/add-comment", methods=["POST"])
@login_required
def create_comment():
    post_Id = request.form.get("post_Id")
    comentario = request.form.get("comentario")
    user_Id = current_user.usuario_Id
    
    try:
        comment = createComment(post_id=post_Id, comentario=comentario, usuario_Id=user_Id)
        if not comment:
            return jsonify({"message": "No se ha creado el comentario", "status": 400}), 400
        return jsonify({"message": "Comentario creado correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})

@comments.route("/api/update-comment/<int:id>", methods=["PUT"])
@login_required
def update_comment(id):
    data = request.form.to_dict()

    try:
        comment = updateComment(id=id, data=data)
        if not comment:
            return jsonify({"message": "No se ha actualizado el comentario", "status": 400}), 400
        return jsonify({"message": "Comentario actualizado correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})        
    
@comments.route("/api/delete-comment/<int:id>", methods=["DELETE"])
@login_required
def delete_comment(id):
    try:
        comment = deleteComment(id=id)
        if not comment:
            return jsonify({"message": "No se ha eliminado el comentario", "status": 400}), 400
        return jsonify({"message": "Comentario eliminado correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})        