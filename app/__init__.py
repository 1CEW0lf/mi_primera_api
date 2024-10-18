#importamos la libreria Flask
from flask import Flask # type: ignore
from flask_restful import Api # type: ignore
from .routes import APIRoutes

#creamos una función para montar el servidor
def crear_app():
    app = Flask(__name__)
    api = Api(app)

    routes = APIRoutes()
    routes.init_routes(api)

#regresamos el servidor montado
    return app