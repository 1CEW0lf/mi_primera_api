from flask_restful import Resource # type: ignore

class HelloWorld(Resource):
    def get(self):
        return {message: 'Hola mundo desde la API', status: 200} # type: ignore
    
class APIRoutes():
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')