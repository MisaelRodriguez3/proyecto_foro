from src.models import db
from datetime import datetime, timezone

class Comment(db.Model):
    __tablename__ = "comentarios"

    comentario_Id = db.Column(db.Integer, primary_key = True)
    comentario = db.Column(db.Text, nullable = False)
    post_Id = db.Column(db.Integer, db.ForeignKey("posts.post_Id"), nullable = False)
    usuario_Id = db.Column(db.Integer, db.ForeignKey("usuarios.usuario_Id"), nullable = False)
    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"{self.comentario_Id}"
    
    def __init__(self, comentario, post_Id, usuario_Id):
        self.comentario = comentario
        self.post_Id = post_Id
        self.usuario_Id = usuario_Id