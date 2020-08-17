from collections import deque
from copy import copy #hacer copias de objetos
from Proyecto20201.Clases.Vertice import *
from Proyecto20201.Clases.Arista import *

class Grafo():
    def __init__(self):
        self.grafodirigido=False
        self.pozos = 0
        self.fuentes = 0
        self.ListaFuentes=[]
        self.ListaVertices=[]
        self.ListaAristas=[]
        self.ListaBloqueados=[]
        self.ListaVisitados=[]

    def getFuentes(self):
        return self.fuentes

    def getListaFuentes(self):
        return self.ListaFuentes

    def getPozos(self):
        return self.pozos

    def getgrafoDirigido(self):
        return self.grafodirigido

    def getListaBloqueados(self):
        return self.ListaBloqueados

    def setListaBloqueados(self,lista):
        self.ListaBloqueados=lista

    def eliminarArista(self,origen,destino):
        for Arista in self.getListaAristas():
            if Arista.getOrigen() == origen and Arista.getDestino() == destino:
                verticeorigen = self.obtenervertice(Arista.getOrigen())
                verticedestino = self.obtenervertice(Arista.getDestino())
                self.getListaAristas().remove(Arista)
                verticeorigen.getListaAdyacentes().remove(verticedestino.getDato())
                verticedestino.getListaIncidentes().remove(verticeorigen.getDato())

    def agregarBloqueada(self,origen,destino):
        self.getListaBloqueados().append(self.obtenerarista(origen,destino))

    def eliminarBloqueada(self,origen,destino):
        for Arista in self.getListaBloqueados():
            if Arista.getOrigen() == origen and Arista.getDestino() == destino:
                self.getListaBloqueados().remove(Arista)

    def obteneraristabloqueada(self, origen, destino):
        for Arista in self.getListaBloqueados():
            if Arista.getOrigen() == origen and Arista.getDestino() == destino:
                return Arista
        return None

    def desbloqueararista(self,origen,destino):
        des=self.obteneraristabloqueada(origen,destino)
        self.getListaAristas().append(des)
        self.eliminarBloqueada(origen,destino)

    def verificararistabloqueada(self, origen, destino):
        for Arista in self.getListaBloqueados():
            if Arista.getOrigen() == origen and Arista.getDestino() == destino:
                return True
        return False

    def getListaAristas(self):
        return self.ListaAristas

    def getListaVertices(self):
        return self.ListaVertices

    def ingresarvertice(self,dato,coordenadas):
        if self.obtenervertice(dato)==None:
            self.ListaVertices.append(Vertice(dato,coordenadas))

    def obtenervertice(self,dato):
        for vertice in self.ListaVertices:
            if vertice.getDato()==dato:
                return vertice
        return None

    def ingresararista(self, origen,destino,peso,dirigido):
        if not self.verificararista(origen,destino):
            if self.obtenervertice(origen) != None and self.obtenervertice(destino) != None:
                self.ListaAristas.append(Arista(origen,destino,peso))
                self.obtenervertice(origen).getListaAdyacentes().append(destino)
                self.obtenervertice(destino).getListaIncidentes().append(origen)
                if not dirigido:
                    self.ListaAristas.append(Arista(destino, origen, peso))
                    self.obtenervertice(destino).getListaAdyacentes().append(origen)
                    self.obtenervertice(origen).getListaIncidentes().append(destino)
                    self.grafodirigido=False

    def obtenerarista(self,origen,destino):
        for Arista in self.ListaAristas:
            if Arista.getOrigen()==origen and Arista.getDestino()==destino:
                return Arista
        return None

    def verificararista(self,origen,destino):
        for Arista in self.ListaAristas:
            if Arista.getOrigen()==origen and Arista.getDestino()==destino:
                return True
        return False

    def imprimirvertice(self):
        for Vertice in self.ListaVertices:
            print("---------------")
            print(Vertice.getDato())
            print("Lista adyacentes", Vertice.getListaAdyacentes())
            print("lista incidentes", Vertice.getListaIncidentes())
            print("Grado de entrada", Vertice.gradoentrada())
            print("Grado de salida", Vertice.gradosalida())

    def profundidad(self,dato):
        if dato in self.ListaVisitados:
            return
        else:
            Vertice = self.obtenervertice(dato)
            if Vertice!=None:
                self.ListaVisitados.append(Vertice.getDato())
                for dato in Vertice.getListaAdyacentes():
                    self.profundidad(dato)

    def getListaVisitados(self):
        return self.ListaVisitados

    def numerodepozos(self):
        for Vertice in self.ListaVertices:
            if(not Vertice.getListaAdyacentes()):
                self.pozos=self.pozos+1
        return self.pozos

    def numerodefuentes(self):
        for Vertice in self.ListaVertices:
            if(not Vertice.getListaIncidentes()):
                self.ListaFuentes.append(Vertice)
                self.fuentes=self.fuentes+1
        return self.fuentes

    def esfdconexo(self,pozos,fuentes):
        if(pozos!=0 or fuentes!=0):
            return "El Grafo es"+"\n"+" Debilmente Conexo"
        else:
            return "El Grafo es"+"\n"+" Fuertemente Conexo"

    def imprimiraristas(self):
        for Arista in self.ListaAristas:
            print("Origen: {0} - Destino: {1} - Peso: {2}".format(Arista.getOrigen(),Arista.getDestino(),Arista.getPeso()))

    def amplitud(self,origen):
        VisitadosA=[]
        cola=deque()
        Vertice=self.obtenervertice(origen)
        if Vertice!=None:
            VisitadosA.append(origen)
            cola.append(Vertice)
        while cola:
            elemento=cola.popleft()#saca el primer elemento de la cola
            for Adyacencia in elemento.getListaAdyacentes():
                if Adyacencia not in VisitadosA:
                    Vertice=self.obtenervertice(Adyacencia)
                    VisitadosA.append(Adyacencia)
                    cola.append(Vertice)
        return VisitadosA

    def verificarvertice(self,dato):
        for vertice in self.ListaVertices:
            if vertice.getDato() == dato:
                return True
        return False

    def ordenamiento(self,CopiaAristas):#Ordeno de menor a mayor
        for i in range(len(CopiaAristas)):
            for j in range(len(CopiaAristas)):
                if CopiaAristas[i].getPeso() < CopiaAristas[j].getPeso():
                    temp=CopiaAristas[i]
                    CopiaAristas[i]=CopiaAristas[j]
                    CopiaAristas[j]=temp

    def Prim(self, origen):
        if not self.verificarvertice(origen):  # verifico el vertice origen
            return None
        desde = self.obtenervertice(origen)
        listaVisitados = []  # visitados de prim
        listaAristas = []  # aristas de prim
        listaVisitados.append(origen)
        while len(listaVisitados) is not len(self.ListaVertices):  # itero hasta que visitadosprim sea igual a lista de vertices
            aristaMenor = self.buscarAristaMenor(listaVisitados)  # busco la arista menor
            listaAristas.append(aristaMenor)
            listaVisitados.append(aristaMenor.getDestino())
        return listaAristas

    def buscarAristaMenor(self, listaVisitados):
        listaAristasaux = []  # lista auxiliar con las aristas a cada vertice
        for v in listaVisitados:  # recorro los vertices visitados
            vertice = self.obtenervertice(v)
            for aux in vertice.getListaAdyacentes():  # recorro los adyacentes a cada vertice
                if aux not in listaVisitados:  # verifico que cada adyacente ya haya sido visitado
                    arista = self.obtenerarista(v, aux)
                    if arista not in listaAristasaux:
                        listaAristasaux.append(arista)
        self.ordenamiento(listaAristasaux)
        aristaMenor = listaAristasaux[0]
        return aristaMenor

    def Kruskal(self):
        copiaAristas = copy(self.ListaAristas)  # copia de las aristas
        AristasKruskal = []
        ListaConjuntos = []

        self.ordenamiento(copiaAristas)  # ordeno las aristas
        for menor in copiaAristas:
            self.Operacionesconjuntos(menor, ListaConjuntos, AristasKruskal)
        # esta ordenada de mayor a menor
        return AristasKruskal

    def Operacionesconjuntos(self, menor, ListaConjuntos, AristasKruskal):
        encontrado1 = -1
        encontrado2 = -1

        if not ListaConjuntos:  # si esta vacia
            ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
            AristasKruskal.append(menor)

        else:
            for i in range(len(ListaConjuntos)):
                if (menor.getOrigen() in ListaConjuntos[i]) and (menor.getDestino() in ListaConjuntos[i]):
                    return False ##Camino cicliclo

            for i in range(len(ListaConjuntos)):
                if menor.getOrigen() in ListaConjuntos[i]:
                    encontrado1 = i
                if menor.getDestino() in ListaConjuntos[i]:
                    encontrado2 = i

            if encontrado1 != -1 and encontrado2 != -1:
                if encontrado1 != encontrado2:  # si pertenecen a dos conjuntos diferentes
                    # debo unir los dos conjuntos
                    ListaConjuntos[encontrado1].update(ListaConjuntos[encontrado2])
                    ListaConjuntos[encontrado2].clear()  # elimino el conjunto
                    AristasKruskal.append(menor)

            if encontrado1 != -1 and encontrado2 == -1:  # si va unido por un conjunto
                ListaConjuntos[encontrado1].add(menor.getOrigen())
                ListaConjuntos[encontrado1].add(menor.getDestino())
                AristasKruskal.append(menor)

            if encontrado1 == -1 and encontrado2 != -1:  # si va unido por un conjunto
                ListaConjuntos[encontrado2].add(menor.getOrigen())
                ListaConjuntos[encontrado2].add(menor.getDestino())
                AristasKruskal.append(menor)

            if encontrado1 == -1 and encontrado2 == -1:  # si no existe en los conjuntos
                ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                AristasKruskal.append(menor)

    def Boruvka(self):
        copiaNodos = copy(self.ListaVertices)  # copia de los nodos
        copiaAristas = copy(self.ListaAristas)  # copia de las aristas

        AristasBorukvka = []
        ListaConjuntos = []
        bandera = True
        cantidad = 0
        while cantidad > 1 or bandera:
            for Nodo in copiaNodos:
                self.OperacionesconjuntosB(Nodo, ListaConjuntos, AristasBorukvka, copiaAristas)
            bandera = False
            cantidad = self.Cantidadconjuntos(ListaConjuntos)
        return AristasBorukvka

    def Cantidadconjuntos(self, ListaConjuntos):
        cantidad = 0
        for conjunto in ListaConjuntos:
            if len(conjunto) > 0:
                cantidad = cantidad + 1
        return cantidad

    def OperacionesconjuntosB(self, Nodo, ListaConjuntos, AristasBorukvka, copiaAristas):
        encontrado1 = -1
        encontrado2 = -1
        menor = self.Buscarmenor(Nodo, copiaAristas)

        if not menor == None:  # si no esta vacio
            if not ListaConjuntos:  # si esta vacia
                ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                AristasBorukvka.append(menor)
            else:
                for i in range(len(ListaConjuntos)):
                    if (menor.getOrigen() in ListaConjuntos[i]) and (menor.getDestino() in ListaConjuntos[i]):
                        return  ##Camino cicliclo

                for i in range(len(ListaConjuntos)):
                    if menor.getOrigen() in ListaConjuntos[i]:
                        encontrado1 = i
                    if menor.getDestino() in ListaConjuntos[i]:
                        encontrado2 = i

                if encontrado1 != -1 and encontrado2 != -1:
                    if encontrado1 != encontrado2:  # si pertenecen a dos conjuntos diferentes
                        # debo unir los dos conjuntos
                        ListaConjuntos[encontrado1].update(ListaConjuntos[encontrado2])
                        ListaConjuntos[encontrado2].clear()  # elimino el conjunto
                        AristasBorukvka.append(menor)

                if encontrado1 != -1 and encontrado2 == -1:  # si va unido por un conjunto
                    ListaConjuntos[encontrado1].add(menor.getOrigen())
                    ListaConjuntos[encontrado1].add(menor.getDestino())
                    AristasBorukvka.append(menor)

                if encontrado1 == -1 and encontrado2 != -1:  # si va unido por un conjunto
                    ListaConjuntos[encontrado2].add(menor.getOrigen())
                    ListaConjuntos[encontrado2].add(menor.getDestino())
                    AristasBorukvka.append(menor)

                if encontrado1 == -1 and encontrado2 == -1:  # si no existe en los conjuntos
                    ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                    AristasBorukvka.append(menor)

    def Buscarmenor(self, Nodo, copiaAristas):
        temp = []
        for adyacencia in Nodo.getListaAdyacentes():
            for Arista in copiaAristas:
                # busco las aristas de esa lista de adyacencia
                if Arista.getOrigen() == Nodo.getDato() and Arista.getDestino() == adyacencia:
                    temp.append(Arista)
        if temp:  # si no esta vacia
            # una vez obtenga todas las aristas, saco la menor
            self.ordenamiento(temp)  # ordeno las aristas
            # elimin ese destino porque ya lo voy a visitar
            # print("{0}-{1}:{2}".format(temp[0].getOrigen(), temp[0].getDestino(), temp[0].getPeso()))

            Nodo.getListaAdyacentes().remove(temp[0].getDestino())
            return temp[0]  # es la menor

        return None  # es la menor