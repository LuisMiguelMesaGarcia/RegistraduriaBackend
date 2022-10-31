from Modelos.Partido import Partido


class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los Partidos")
        unPartido={
            "_id":"abc123",
            "nombre":"Partido de la bandera",
            "lema":"Comprometidos con la justicia"
        }
        return [unPartido]

    def create(self,infoPartido):
        print("Crear un partido")
        elPartido = Partido(infoPartido)
        return elPartido.__dict__


    def show(self,id):
        print("Mostrando un partido con id ",id)
        elPartido={
            "_id":"abc123",
            "nombre":"Partido de la bandera",
            "lema":"Comprometidos con la justicia"
        }
        return elPartido

    def update(self,id,infoPartido):
        print("Actualizando partido con id ",id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__


    def delete(self,id):
        print("Elimiando Partido con id ",id)
        return {"deleted_count":1}
