from src.models import db
from flask_login import UserMixin
from datetime import datetime, timezone

image = "https://i.pinimg.com/550x/a8/0e/36/a80e3690318c08114011145fdcfa3ddb.jpg"

class User(db.Model, UserMixin):
    __tablename__ = "usuarios"

    usuario_Id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(150), nullable = False)
    correo = db.Column(db.String(120), nullable = False, unique = True)
    usuario = db.Column(db.String(15), nullable = False, unique = True)
    password = db.Column(db.String(200), nullable = False)
    imagen_url = db.Column(db.String(200), nullable = True)
    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))

    #Relaciones
    posts = db.relationship('Post', backref='author', lazy=True)
    materials = db.relationship('Material', backref='author', lazy=True)
    examples = db.relationship('Example', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    challenges = db.relationship('Challenge', backref='author', lazy=True)

    def __repr__(self):
        return f"{self.usuario}"
    
    def __init__(self, nombre, correo, usuario, password, imagen_url=image):
        self.nombre = nombre
        self.correo = correo
        self.usuario = usuario
        self.password = password
        self.imagen_url = imagen_url

    def get_id(self):
        return str(self.usuario_Id)