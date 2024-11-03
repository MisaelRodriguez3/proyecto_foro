from src.models import db

class Topic(db.Model):
    __tablename__ = "temas"

    tema_Id = db.Column(db.Integer, primary_key = True)
    tema = db.Column(db.String(100), nullable = False)
    imagen_url = db.Column(db.String(200), nullable = False)

    #Relaciones
    posts = db.relationship('Post', backref='tema', lazy=True)
    materials = db.relationship('Material', backref='tema', lazy=True)
    examples = db.relationship('Example', backref='tema', lazy=True)
    challenges = db.relationship('Challenge', backref='tema', lazy=True)

    def __repr__(self):
        return f"{self.tema}"
    
    def __init__(self, tema, imagen_url):
        self.tema = tema
        self.imagen_url = imagen_url