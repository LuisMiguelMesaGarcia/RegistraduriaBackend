from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido
class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioPartido.findAll()
    def create(self,infoPartido):
        nuevoPartido=Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)
    def show(self,id):
        elPartido=Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__
    def update(self,id,infoPartido):
        partidoActual=Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)
    def delete(self,id):
        return self.repositorioPartido.delete(id)

































"""
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
"""