from src.models import db
from datetime import datetime, timezone

class Material(db.Model):
    __tablename__ = "materiales"

    material_Id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(200), nullable = False)
    descripcion = db.Column(db.Text, nullable = False)
    material_url = db.Column(db.String(200), nullable = False)
    tema_Id = db.Column(db.Integer, db.ForeignKey("temas.tema_Id"), nullable = False)
    usuario_Id = db.Column(db.Integer, db.ForeignKey("usuarios.usuario_Id"), nullable = False)
    es_externo = db.Column(db.Boolean, default = False)
    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"{self.titulo}"
    
    def __init__(self, titulo, descripcion, material_url, tema_Id, usuario_Id, es_externo):
        self.titulo = titulo
        self.descripcion = descripcion
        self.material_url = material_url
        self.tema_Id = tema_Id
        self.es_externo = es_externo
        self.usuario_Id = usuario_Id