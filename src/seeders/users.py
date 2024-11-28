from decouple import config
from src.models import User
from src.service import createUser

def createFirstUser():
    user = User.query.filter_by(usuario="tester00").first()
    if not user:
        try:
            tester = createUser(config("USER"), config("USER_EMAIL"), config("USER_NICKNAME"), config("USER_PASSWORD"))
            print("Usuario creado")
        except Exception as e:
            print(f"Error al crear el usuario: {e}")