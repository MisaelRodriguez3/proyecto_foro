from src.models import Topic
from src.service import createTopic

topics = [
    {"nombre": "python", "imagen": "https://i0.wp.com/junilearning.com/wp-content/uploads/2020/06/python-programming-language.webp?fit=800%2C800&ssl=1"},
    {"nombre": "java", "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2GBqKlTgJ9SzYYObejYZNMFYB9QrjQ-Spsw&s"},
    {"nombre": "javascript", "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/800px-JavaScript-logo.png"},
    {"nombre": "html", "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/800px-HTML5_logo_and_wordmark.svg.png"},
    {"nombre": "css", "imagen": "https://www.svgrepo.com/show/452185/css-3.svg"},
]

def insertTopics():
    _topics = Topic.query.all()
    if not _topics:

        for topic in topics:
            new_topic = createTopic(nombre=topic["nombre"], imagen=topic["imagen"])
            print(f"tema {new_topic.tema} creado")
        print("Temas creados")