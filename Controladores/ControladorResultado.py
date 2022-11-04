
from Repositorios.RepositorioResultado import RepositorioResultado
from Modelos.Resultado import Resultado
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
    def index(self):
        return self.repositorioResultado.findAll()
    def create(self,infoResultado):
        nuevoResultado=Resultado(infoResultado)
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    def update(self,id,infoResultado):
        resultadoActual=Resultado(self.repositorioResultado.findById(id))
        resultadoActual.numero_mesa = infoResultado["numero_mesa"]
        resultadoActual.id_partido = infoResultado["id_partido"]
        return self.repositorioResultado.save(resultadoActual)
    def delete(self,id):
        return self.repositorioResultado.delete(id)







"""

from Modelos.Resultado import Resultado


class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        print("Listar todos los Resultados")
        unResultado = {
            "id": "123qwe",
            "numero_mesa": "1",
            "id_partido": "abc123",
        }
        return [unResultado]

    def create(self, infoResultado):
        print("Crear un resultado")
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def show(self, id):
        print("Mostrando un resultado con id ", id)
        elResultado = {
            "id": "123qwe",
            "numero_mesa": "1",
            "id_partido": "abc123",
        }
        return elResultado

    def update(self, id, infoResultado):
        print("Actualizando resultado con id ", id)
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def delete(self, id):
        print("Elimiando Resultado con id ", id)
        return {"deleted_count": 1}


"""