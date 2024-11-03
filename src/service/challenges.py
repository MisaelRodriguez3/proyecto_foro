from src.models import db, Challenge, Topic
from sqlalchemy import or_

def getChallenge(id):
    try:
        return Challenge.query.get(id)
    except Exception as e:
        print("Error: ", e)
        return None

def getAllChallengesByTopic(tema):
    try:
        topic = Topic.query.filter_by(tema=tema).first()
        if not topic:
            return None
        challenges = Challenge.query.filter_by(tema_Id=topic.tema_Id).order_by(Challenge.created_at.desc()).all()
        if not challenges:
            return None
        return challenges
    except Exception as e:
        print("Error: ", e)
        return None
    
def createChallenge(titulo, descripcion, dificultad, tema, usuario_Id):
    try:
        topic = Topic.query.filter_by(tema=tema).first()
        if not topic:
            return None
        challenge = Challenge(titulo=titulo, descripcion=descripcion, dificultad=dificultad, tema_Id=topic.tema_Id, usuario_Id=usuario_Id)
        db.session.add(challenge)
        db.session.commit()
        return challenge
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def updateChallenge(id, data):
    try:
        challenge = Challenge.query.get(id)
        if not challenge:
            return None
        for field, value in data.items():
            if hasattr(challenge, field) and field != "id":
                setattr(challenge, field, value)
        db.session.commit()
        return f"Reto {challenge.reto_Id} actualizado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def deleteChallenge(id):
    try:
        challenge = Challenge.query.get(id)
        if not challenge:
            return None
        db.session.delete(challenge)
        db.session.commit()
        return f"Reto {challenge.reto_Id} eliminado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def searchChallenge(text):
    try:
        challenges = Challenge.query.filter(or_(
            Challenge.titulo.ilike(f"%{text}%"),
            Challenge.descripcion.ilike(f"%{text}%"),
            Challenge.dificultad.ilike(f"%{text}%")
        )).all()

        if not challenges:
            return None
        return challenges
    except Exception as e:
        print("Error: ", e)
        return None