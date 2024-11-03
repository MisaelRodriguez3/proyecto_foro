from src.models import db, Topic

def getTopics():
    try:
        return Topic.query.all()
    except Exception as e:
        return f"Error al obtener los temas: {e}"
    
def createTopic(nombre, imagen):
    try:
        topic = Topic(tema=nombre, imagen_url=imagen)
        db.session.add(topic)
        db.session.commit()
        return topic
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def updateTopic(id, data):
    try:
        topic = Topic.query.get(id)
        if not topic:
            return None
        for field, value in data.items():
            if hasattr(topic, field) and field != "id":
                setattr(topic, field, value)
        db.session.commit()
        return f"Tema {topic.tema} actualizado"
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def deleteTopic(id):
    try:
        topic = Topic.query.get(id)
        if not topic:
            return None
        db.session.delete(topic)
        db.session.commit()
        return f"Tema {topic.tema} eliminado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None