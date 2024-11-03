from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from src.service.posts import createPost, updatePost, deletePost

posts = Blueprint("posts", __name__)

@posts.route("/api/add-post", methods=["POST"])
@login_required
def create_post():
    titulo = request.form.get("titulo")
    descripcion = request.form.get("descripcion")
    tema = request.form.get("topic")
    codigo = request.form.get("codigo", None)
    user_Id = current_user.usuario_Id

    try:
        post = createPost(titulo=titulo, descripcion=descripcion, tema=tema, usuario_Id=user_Id, codigo=codigo)
        if not post:
            return jsonify({"message": "No se ha creado la publicación", "status": 400}), 400
        return jsonify({"message": "Publicación creada correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)}), 500
    
@posts.route("/api/update-post/<int:id>", methods=["PUT"])
@login_required
def update_post(id):
    data = request.form.to_dict()
    try:
        post = updatePost(id=id, data=data)
        if not post:
            return jsonify({"message": "No se ha actualizado la publicación", "status": 400}), 400
        return jsonify({"message": "Publicación actualizada correctamente", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})
    
@posts.route("/api/delete-post/<int:id>", methods=["DELETE"])
@login_required
def delete_post(id):
    try:
        post = deletePost(id=id)
        if not post:
            return jsonify({"message": "No se ha eliminado la publicación.", "status": 400}), 400
        return jsonify({"message": "Publicación eliminada", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal.", "status": 500, "error": str(e)})