from src.models import db, Comment, Post

def getCommentsByPost(post_id):
    try:
        post = Post.query.get(post_id)
        if not post:
            return None
        comments = Comment.query.filter_by(post_Id=post.post_Id).all()
        if not comments:
            return None
        return comments
    except Exception as e:
        print("Error: ", e)
        return None
    
def createComment(post_id, comentario, usuario_Id):
    try:
        comment = Comment(comentario=comentario, post_Id=post_id, usuario_Id=usuario_Id)
        db.session.add(comment)
        db.session.commit()
        return comment
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def updateComment(id, data):
    try:
        comment = Comment.query.get(id)
        if not comment:
            return None
        for field, value in data.items():
            if hasattr(comment, field) and field != "id":
                setattr(comment, field, value)
        db.session.commit()
        return f"Comenatrio {comment.comentario_Id} actualizado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None

def deleteComment(id):
    try:
        comment = Comment.query.get(id)
        if not comment:
            return None
        db.session.delete(comment)
        db.session.commit()
        return f"Comentario {comment.comenatario_id} eliminado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None