from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevoMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)
    def show(self,id):
        elMesa=Mesa(self.repositorioMesa.findById(id))
        return elMesa.__dict__
    def update(self,id,infoMesa):
        mesaActual=Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)



"""

from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todas las Mesas")
        unMesa={
            "_id":"abc123",
            "nombre":"Mesa de la bandera",
            "lema":"Comprometidos con la justicia"
        }
        return [unMesa]

    def create(self, infoMesa):
        print("Crear una mesa")
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__


    def show(self,id):
        print("Mostrando una mesa con id ",id)
        elMesa={
            "_id":"abc123",
            "nombre":"Mesa de la bandera",
            "lema":"Comprometidos con la justicia"
        }
        return elMesa

    def update(self,id,infoMesa):
        print("Actualizando mesa con id ",id)
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__


    def delete(self,id):
        print("Elimiando Mesa con id ",id)
        return {"deleted_count":1}
"""