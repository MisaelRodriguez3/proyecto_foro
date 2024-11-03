from src.models import db, Example, Topic
from sqlalchemy import or_

def getExample(id):
    try:
        return Example.query.get(id)
    except Exception as e:
        print("Error: ", e)
        return None
    
def getAllExamplesByTopic(tema):
    try:
        topic = Topic.query.filter_by(tema=tema).first()
        if not topic:
            return None
        
        examples = Example.query.filter_by(tema_Id=topic.tema_Id).order_by(Example.created_at.desc()).all()
        if not examples:
            return None
        return examples
    except Exception as e:
        print("Error: ", e)
        return None
    
def createExample(titulo, descripcion, tema, usuario_Id, codigo=None):
    try:
        topic = Topic.query.filter_by(tema=tema).first()
        if not topic:
            raise ValueError("Tema no encontrado")
        example = Example(titulo=titulo, descripcion=descripcion, codigo=codigo, tema_Id=topic.tema_Id, usuario_Id=usuario_Id)
        db.session.add(example)
        db.session.commit()
        return example
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def updateExample(id, data):
    try:
        example = Example.query.get(id)
        if not example:
            return None
        for field, value in data.items():
            if hasattr(example, field) and field != "id":
                setattr(example, field, value)
        db.session.commit()
        return f"Ejemplo {example.ejemplo_Id} actualizado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def deleteExample(id):
    try:
        example = Example.query.get(id)
        if not example:
            return None
        db.session.delete(example)
        db.session.commit()
        return f"Ejemplo {example.ejemplo_Id} eliminado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def searchExample(text):
    try:
        examples = Example.query.filter(or_(
            Example.titulo.ilike(f"%{text}%"),
            Example.descripcion.ilike(f"%{text}%"),
            Example.codigo.ilike(f"%{text}%")
        )).all()

        if not examples:
            return None
        return examples
    except Exception as e:
        print("Error: ", e)
        return None