from src.models import db
from datetime import datetime, timezone

class Challenge(db.Model):
    __tablename__ = "retos"

    reto_Id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(200), nullable = False)
    descripcion = db.Column(db.Text, nullable = False)
    dificultad = db.Column(db.String(20), nullable = False)
    tema_Id = db.Column(db.Integer, db.ForeignKey("temas.tema_Id"), nullable = False)
    usuario_Id = db.Column(db.Integer, db.ForeignKey("usuarios.usuario_Id"), nullable = False)
    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"{self.titulo}"
    
    def __init__(self, titulo, descripcion, dificultad, tema_Id, usuario_Id):
        self.titulo = titulo
        self.descripcion = descripcion
        self.dificultad = dificultad
        self.tema_Id = tema_Id
        self.usuario_Id = usuario_Id