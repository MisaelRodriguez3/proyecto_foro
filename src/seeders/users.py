from src.models import User
from src.service import createUser

def createFirstUser():
    user = User.query.filter_by(usuario="tester00").first()
    if not user:
        try:
            tester = createUser("el tester", "tester00@gmail.com", "tester00", "tester00")
            print("Usuario creado")
        except Exception as e:
            print(f"Error al crear el usuario: {e}")