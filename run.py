#importamos el servidor montado
from app import crear_app

#corremos el servidor
crear_app().run(debug=True, port=5050)