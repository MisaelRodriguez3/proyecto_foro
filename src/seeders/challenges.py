from src.models import Challenge
from src.service import createChallenge

challenges = [
    {
        "titulo": "Generador de contraseñas seguras",
        "descripcion": "Crea un programa que genere contraseñas aleatorias seguras, utilizando letras mayúsculas, minúsculas, números y símbolos. El usuario debe poder especificar la longitud de la contraseña.",
        "dificultad": "intermedio", 
        "tema": "python",
        "usuario_Id": 1
    },
    {
        "titulo": "Calculadora de Fibonacci",
        "descripcion": "Escribe una función que reciba un número n y devuelva el n-ésimo número en la secuencia de Fibonacci. La función debe ser eficiente, utilizando recursión o programación dinámica.",
        "dificultad": "avanzado", 
        "tema": "python",
        "usuario_Id": 1
    },
    {
        "titulo": "Juego de Adivinanza de Números",
        "descripcion": "Crea un programa en Java que permita al usuario adivinar un número aleatorio entre 1 y 100. El programa debe dar pistas sobre si el número es mayor o menor que la elección del usuario hasta que adivine correctamente.",
        "dificultad": "facil", 
        "tema": "java",
        "usuario_Id": 1
    },
    {
        "titulo": "Implementación de una Pila (Stack)",
        "descripcion": "Implementa una pila en Java utilizando arreglos o listas enlazadas. La pila debe soportar las operaciones básicas: push, pop, y peek.",
        "dificultad": "intermedio", 
        "tema": "java",
        "usuario_Id": 1
    },
    {
        "titulo": "Contador de caracteres en una cadena",
        "descripcion": "Crea un programa en JavaScript que cuente cuántos caracteres tiene una cadena de texto introducida por el usuario. El programa debe excluir los espacios en blanco.",
        "dificultad": "facil", 
        "tema": "javascript",
        "usuario_Id": 1
    },
    {
        "titulo": "Validación de formulario",
        "descripcion": "Desarrolla un script que valide un formulario en HTML con campos de nombre, correo electrónico y mensaje. El correo electrónico debe seguir un formato adecuado y los campos no deben estar vacíos.",
        "dificultad": "intermedio", 
        "tema": "javascript",
        "usuario_Id": 1
    },
    {
        "titulo": "Crear una página de perfil de usuario",
        "descripcion": "Desarrolla una página de perfil de usuario utilizando HTML donde se muestren detalles como nombre, foto de perfil, biografía y un enlace a redes sociales.",
        "dificultad": "facil", 
        "tema": "html",
        "usuario_Id": 1
    },
    {
        "titulo": "Tabla con clasificación interactiva",
        "descripcion": "Crea una tabla HTML que permita al usuario ordenar los datos por columnas, como nombre o edad. Usa HTML para la estructura y JavaScript para la funcionalidad de clasificación.",
        "dificultad": "intermedio", 
        "tema": "html",
        "usuario_Id": 1
    },
    {
        "titulo": "Efecto Parallax",
        "descripcion": "Implementa un efecto parallax en una página web utilizando CSS. Los elementos de fondo deben desplazarse a una velocidad diferente que los elementos del primer plano cuando se hace scroll.",
        "dificultad": "avanzado", 
        "tema": "css",
        "usuario_Id": 1
    },
    {
        "titulo": "Crear una tarjeta de perfil",
        "descripcion": "Usa CSS para diseñar una tarjeta de perfil con imagen, nombre y breve descripción. La tarjeta debe tener bordes redondeados, sombra y un efecto hover para cambiar el color de fondo.",
        "dificultad": "facil", 
        "tema": "css",
        "usuario_Id": 1
    }
]

def insertChallenges():
    _challenges = Challenge.query.all()
    if not _challenges:
        for challenge in challenges:
            new_challenge = createChallenge(
                titulo=challenge["titulo"],
                descripcion=challenge["descripcion"],
                dificultad=challenge["dificultad"],
                tema=challenge["tema"],
                usuario_Id=challenge["usuario_Id"]
            )
            print(f"Reto {new_challenge.reto_Id} creado")
        print("Retos creados")