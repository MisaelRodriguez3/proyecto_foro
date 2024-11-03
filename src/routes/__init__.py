# Importaciones rutas del servido
from src.routes.server.auth import auth
from src.routes.server.posts import posts
from src.routes.server.challenges import challenges
from src.routes.server.comments import comments
from src.routes.server.examples import examples
#from src.routes.server.material import 

# Importaciones rutas del cliente
from src.routes.client.auth import auth as auth_client
from src.routes.client.user import user as user_client
from src.routes.client.others import other as other_client

def register_routes(app):
    # Server Routes
    app.register_blueprint(auth)
    app.register_blueprint(posts)
    app.register_blueprint(challenges)
    app.register_blueprint(comments)
    app.register_blueprint(examples)



    # Client Routes
    app.register_blueprint(auth_client)
    app.register_blueprint(user_client)
    app.register_blueprint(other_client)