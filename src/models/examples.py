from src.models import db
from datetime import datetime, timezone

class Example(db.Model):
    __tablename__ = "ejemplos"

    ejemplo_Id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(200), nullable = False)
    descripcion = db.Column(db.Text, nullable = False)
    codigo = db.Column(db.Text, nullable = False)
    tema_Id = db.Column(db.Integer, db.ForeignKey("temas.tema_Id"), nullable = False)
    usuario_Id = db.Column(db.Integer, db.ForeignKey("usuarios.usuario_Id"), nullable = False)
    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"{self.titulo}"
    
    def __init__(self, titulo, descripcion, codigo, tema_Id, usuario_Id):
        self.titulo = titulo
        self.descripcion = descripcion
        self.codigo = codigo
        self.tema_Id = tema_Id
        self.usuario_Id = usuario_Id