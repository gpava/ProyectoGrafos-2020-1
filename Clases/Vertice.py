
class Vertice:

    def __init__(self, dato,
                 coordenates=[]):
        self.dato = dato
        self.ListaAdyacentes = []
        self.ListaIncidentes = []
        self.coordenates = coordenates

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getCoordenates(self):
        return self.coordenates

    def getListaAdyacentes(self):
        return self.ListaAdyacentes

    def setListaAdyacentes(self, lista):
        self.ListaAdyacentes = lista

    def setListaIncidentes(self, lista):
        self.ListaIncidentes = lista

    def getListaIncidentes(self):
        return self.ListaIncidentes

    def gradoentrada(self):
        return len(self.ListaIncidentes)

    def gradosalida(self):
        return len(self.ListaAdyacentes)