from flask import Blueprint, request, jsonify
from src.service import loginUser, registerUser, logoutUser, updateUser
from flask_login import login_required

auth = Blueprint("auth", __name__)

@auth.route("/api/login", methods=["POST"])  # Asegúrate de que la ruta sea correcta
def login():
        correo = request.form.get("correo")
        password = request.form.get("password")

        # Verificar credenciales
        try: 
            usuario = loginUser(correo=correo, password=password)
            if not usuario:
                return jsonify({"message": "Credenciales inválidas.", "status": 401}), 401     
            return jsonify({"message": "Inicio de sesión exitoso", "status": 200}), 200
        except Exception as e:
             return jsonify({"message": "Algo salió mal", "status": 500, "error": e}),500


@auth.route("/api/register", methods=["POST"])
def register():
    nombre = request.form.get("fullname")
    usuario = request.form.get("username")
    correo = request.form.get("email")
    password = request.form.get("password")

    try:
        user = registerUser(nombre=nombre, usuario=usuario, correo=correo, password=password)
        if not user:
             return jsonify({"message": "Algo salió mal.", "status": 401}), 401
        return jsonify({"message": "Registro exitoso", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal", "status": 500, "error": str(e)}), 500

@auth.route("/api/logout", methods=["POST"])
@login_required
def logout():
    try:
        logoutUser()
        return jsonify({"message": "Sesión cerrada", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal", "status": 500, "error": str(e)}), 500
    
@auth.route("/api/update-profile/<int:id>", methods=["PUT"])
@login_required
def update_profile(id):
    data = request.form.to_dict()
    try:
        user = updateUser(id=id, data=data)
        if not user:
             return jsonify({"message": "No se actualizó el perfil.", "status": 401}), 401
        return jsonify({"message": "Actualización exitosa", "status": 200}), 200
    except Exception as e:
        return jsonify({"message": "Algo salió mal", "status": 500, "error": str(e)}), 500