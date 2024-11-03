from src.models import db, User
from src.service import createUser
from werkzeug.security import check_password_hash
from flask_login import current_user, login_user, logout_user

def loginUser(correo, password):
    try:
        user = User.query.filter_by(correo=correo).first()
        if not user:
            return None
        isMatch = check_password_hash(user.password, password)
        if not isMatch:
            return None
        login_user(user=user, remember=True)
        return current_user
    except Exception as e:
        print("error:", e)
        return None
    
def registerUser(nombre, correo, usuario, password):
    try:
        user =createUser(nombre=nombre, correo=correo, usuario=usuario, password=password)
        login_user(user=user, remember=True)
        return current_user
    except Exception as e:
        print("error:", e)
        db.session.rollback()
        return None
    
def logoutUser():
    logout_user()
    return "Log out"