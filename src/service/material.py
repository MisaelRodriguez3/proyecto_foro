from src.models import db, Material, Topic

def getMaterial(id):
    try:
        material = Material.query.get(id)
        if not material:
            return None
        return material
    except Exception as e:
        print("Error: ", e)
        return None
    
def getAllMaterialsByTopic(tema):
    try:
        topic = Topic.query.filter_by(tema=tema).first()
        if not topic:
            return None
        
        materials = Material.query.filter_by(tema_id=topic.tema_Id).order_by(Material.created_at.desc()).all()
        if not materials:
            return None
        return materials
    except Exception as e:
        print("Error: ", e)
        return None
    
def createMaterial(titulo, descripcion, material_url, tema_Id, usuario_Id, es_externo=False):
    try:
        material = Material(titulo=titulo, descripcion=descripcion, material_url=material_url, tema_Id=tema_Id, usuario_Id=usuario_Id, es_externo=es_externo)
        db.session.add(material)
        db.session.commit()
        return material
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
    
def updateMaterial(id, data):
    try:
        material = Material.query.get(id)
        if not material:
            return None
        for field, value in data.items():
            if hasattr(material, field) and field != "id":
                setattr(material, field, value)
        db.session.commit()
        return f"Material {material.titulo} actualizado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None

def deleteMaterial(id):
    try:
        material = Material.query.get(id)
        if not material:
            return None
        db.session.delete(material)
        db.session.commit()
        return f"Material {material.titulo} eliminado."
    except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None