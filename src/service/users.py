from src.models import db, User
from werkzeug.security import generate_password_hash

def getUser(id):
    try:
        return User.query.get(id)
    except Exception as e:
        print("Error: ", e)
        return None
    
def createUser(nombre, correo, usuario, password):
    try:
        passHash = generate_password_hash(password)
        user = User(nombre=nombre, correo=correo, usuario=usuario, password=passHash)
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        db.session.rollback()
        return None
    
def updateUser(id, data):
    try:
        user = User.query.get(id)
        if not user:
            return None
        for field, value in data.items():
            if hasattr(user, field) and field != "id":
                setattr(user, field, value)
        db.session.commit()
        return f"Usuario {user.usuario} actualizado"
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def deleteUser(id):
    try:
        user = User.query.get(id)
        if not user:
            return None
        db.session.delete(user)
        db.session.commit()
        return f"Usuario {user.usuario} eliminado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None