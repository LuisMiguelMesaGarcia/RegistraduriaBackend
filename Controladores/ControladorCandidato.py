from Modelos.Candidato import Candidato


class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        print("Listar todos los Candidatos")
        unCandidato = {
            "cedula": "12345",
            "numero_resolucion": "XD123",
            "nombre": "Juan",
            "apellido": "Pato"
        }
        return [unCandidato]

    def create(self, infoCandidato):
        print("Crear un candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self, id):
        print("Mostrando un candidato con id ", id)
        elCandidato = {
            "cedula": "12345",
            "numero_resolucion": "XD123",
            "nombre": "Juan",
            "apellido": "Pato"
        }
        return elCandidato

    def update(self, id, infoCandidato):
        print("Actualizando candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Elimiando Candidato con id ", id)
        return {"deleted_count": 1}
