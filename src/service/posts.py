from src.models import db, Post, Topic
from sqlalchemy import or_

def getPost(id):
    try:
        return Post.query.get(id)
    except Exception as e:
        print("Error: ", e)
        return None
    
def getAllPosts():
    try:
        return Post.query.order_by(Post.created_at.desc()).all()
    except Exception as e:
        print("Error: ", e)
        return None
    
def getAllPostByTopic(tema):
    try:
        topic = Topic.query.filter_by(tema=tema).first()
        if not topic:
            return None
        
        posts = Post.query.filter_by(tema_Id=topic.tema_Id).order_by(Post.created_at.desc()).all()
        if not posts:
            return None
        return posts
    except Exception as e:
        print("Error: ", e)
        return None
    
def getAllPostByUser(user_Id):
    try:
        return Post.query.filter_by(usuario_Id=user_Id).order_by(Post.created_at.desc()).limit(5).all()
    except Exception as e:
        print("Error: ", e)
        return None


def createPost(titulo, descripcion, tema, usuario_Id, codigo=""):
    try:
        topic = Topic.query.filter_by(tema=tema).first()
        if not topic:
            raise ValueError("Tema no encontrado")

        post = Post(titulo=titulo, descripcion=descripcion, tema_Id=topic.tema_Id, usuario_Id=usuario_Id, codigo=codigo)
        db.session.add(post)
        db.session.commit()
        return post
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None

def updatePost(id, data):
    try:
        post = Post.query.get(id)
        if not post:
            return None
        for field, value in data.items():
            if hasattr(post, field) and field != "id":
                setattr(post, field, value)
        db.session.commit()
        return f"Publicación {post.post_Id} actualizado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def deletePost(id):
    try:
        post = Post.query.get(id)
        if not post:
            return None
        db.session.delete(post)
        db.session.commit()
        return f"Publicación {post.post_Id} eliminada."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def searchPost(text):
    try:
        posts = Post.query.filter(or_(
            Post.titulo.ilike(f"%{text}%"),
            Post.descripcion.ilike(f"%{text}%"),
            Post.codigo.ilike(f"%{text}%")
        )).all()

        if not posts:
            return None
        return posts
    except Exception as e:
        print("Error: ", e)
        return None