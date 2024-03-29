from collections import deque
from copy import copy #hacer copias de objetos
from Proyecto20201.Clases.Vertice import *
from Proyecto20201.Clases.Arista import *

class Grafo():
    def __init__(self):
        self.pozos = 0
        self.fuentes = 0
        self.ListaFuentes=[]
        self.ListaVertices=[]
        self.ListaAristas=[]
        self.ListaBloqueados=[]
        self.ListaVisitados=[]

    def getFuentes(self):
        return self.fuentes

    def setFuentes(self,fuente):
         self.fuentes = fuente

    def getListaFuentes(self):
        return self.ListaFuentes

    def setListaFuentes(self,lista):
        self.ListaFuentes = lista

    def getPozos(self):
        return self.pozos

    def setPozos(self,pozos):
        self.pozos = pozos

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
            if not Vertice.getListaAdyacentes():
                self.pozos=self.pozos+1
        return self.pozos

    def numerodefuentes(self):
        for Vertice in self.ListaVertices:
            if not Vertice.getListaIncidentes():
                self.ListaFuentes.append(Vertice)
                self.fuentes = self.fuentes + 1
        return self.fuentes

    def inaccesible(self,ListaFuentes):
        for fuente in ListaFuentes:
            for adya in fuente.getListaAdyacentes():
                self.agregarBloqueada(fuente.getDato(), adya)
                self.eliminarArista(fuente.getDato(), adya)

    def fuentesgrafo(self):
        for Vertice in self.ListaVertices:
            if not Vertice.getListaIncidentes():
                self.ListaFuentes.append(Vertice)
                self.fuentes = self.fuentes + 1

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

    def arbolPrim(self):
        CopiaAristas = copy(self.ListaAristas)
        Conjunto = []  # almacena los vertices que voy visitando
        AristasTemp = []  # Aristas temporales (las amarillas)
        Aristasprim = []  # Aristas que van a hacer parte de prim (verdes)
        # self.nodirigido(CopiaAristas) #convierte a grafo no dirigido
        self.ordenamiento(CopiaAristas)
        self.repetidos(CopiaAristas)  # convierte a un grafo dirigido
        menor = CopiaAristas[0]  # Arista menor
        Conjunto.append(menor.getOrigen())  # guardo el primer vertice
        pos = True
        while pos:
            for Vertice in Conjunto:
                self.algoritmo(CopiaAristas, Aristasprim, AristasTemp, Vertice, Conjunto)
                if len(Conjunto) == len(self.ListaVertices):
                    pos = False
        return Aristasprim

    def repetidos(self, CopiaAristas):
        # elimina las direcciones dobles, elimina las aristas no dirigidas y
        # las coniverte en dirigidas
        for elemento in CopiaAristas:
            for i in range(len(CopiaAristas)):
                if elemento.getOrigen() == CopiaAristas[i].getDestino() and elemento.getDestino() == CopiaAristas[i].getOrigen():
                    CopiaAristas.pop(i)
                    break

    def algoritmo(self, CopiaAristas, Aristasprim, AristasTemp, Vertice, Conjunto):
        ciclo = False
        self.agregarAristastemp(CopiaAristas, Vertice, AristasTemp)
        menor = self.menorCandidata(AristasTemp, Aristasprim, CopiaAristas)  # busco la posible candidata
        if menor != None:
            if menor.getOrigen() in Conjunto and menor.getDestino() in Conjunto:  # verifico ciclo
                ciclo = True
            if ciclo == False:
                if not menor.getOrigen() in Conjunto:
                    Conjunto.append(menor.getOrigen())
                if not menor.getDestino() in Conjunto:
                    Conjunto.append(menor.getDestino())
                Aristasprim.append(menor)

    def agregarAristastemp(self, CopiaAristas, Vertice,
                           AristasTemp):  # Agrego las aristas que hacen parte del vertice visitado
        for Arista in CopiaAristas:
            if Vertice == Arista.getDestino() or Vertice == Arista.getOrigen():
                if self.verificarTemp(Arista, AristasTemp):
                    AristasTemp.append(Arista)  # Agrego a temporales o amarillas

    def verificarTemp(self, Arista, AristasTemp):
        for AristaE in AristasTemp:  # verifico que ya este en las amarillas
            if AristaE.getOrigen() == Arista.getDestino() and AristaE.getDestino() == Arista.getOrigen():
                return False
        return True

    def menorCandidata(self, AristasTemp, Aristasprim, CopiaAristas):
        menor = CopiaAristas[
            len(CopiaAristas) - 1]  # es el mayor realmente pero de esta manera realizo los intercambios
        for i in range(len(AristasTemp)):
            if AristasTemp[i].getPeso() < menor.getPeso():
                if self.buscarPrim(Aristasprim, AristasTemp[i]):
                    menor = AristasTemp[i]
        AristasTemp.pop(AristasTemp.index(menor))  # la elimino de las temporales amarillas
        return menor

    def buscarPrim(self, Aristasprim, menor):
        for Aristap in Aristasprim:
            if Aristap.getOrigen() == menor.getOrigen() and Aristap.getDestino() == menor.getDestino():
                return False
            if Aristap.getOrigen() == menor.getDestino() and Aristap.getDestino() == menor.getOrigen():
                return False
        return True

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


    def caminoMasCorto(self, origen, destino):
        VerticesAux = []
        VerticesD = []
        caminos = self.dijkstra(origen, VerticesAux)
        cont = 0
        for i in caminos:
            print("La distancia mínima a: " + self.ListaVertices[cont].getDato() + " es " + str(i))
            cont = cont + 1
        self.rutas(VerticesD, VerticesAux, destino, origen)
        print("El camino más corto de: " + origen + " a " + destino + " es: ")
        print(VerticesD)
        return VerticesD

    def rutas(self,VerticesD, VerticesAux, destino, origen):
        verticeDestino = self.obtenervertice(destino)
        indice = self.ListaVertices.index(verticeDestino)
        if VerticesAux[indice] is None:
            print("No hay camino entre: ", (origen, destino))
            return
        aux = destino
        while aux is not origen:
            verticeDestino = self.obtenervertice(aux)
            indice = self.ListaVertices.index(verticeDestino)
            VerticesD.insert(0, aux)
            aux = VerticesAux[indice]
        VerticesD.insert(0, aux)

    def dijkstra(self, origen, VerticesAux):
        marcados = []  # la lista de los que ya hemos visitado
        caminos = []  # la lista final
        # iniciar los valores en infinito
        for v in self.ListaVertices:
            caminos.append(float("inf"))
            marcados.append(False)
            VerticesAux.append(None)
            if v.getDato() is origen:
                caminos[self.ListaVertices.index(v)] = 0
                VerticesAux[self.ListaVertices.index(v)] = v.getDato()
        while not self.todosMarcados(marcados):
            aux = self.menorNoMarcado(caminos, marcados)  # obtuve el menor no marcado
            if aux is None:
                break
            indice = self.ListaVertices.index(aux)  # indice del menor no marcado
            marcados[indice] = True  # marco como visitado
            valorActual = caminos[indice]
            for vAdya in aux.getListaAdyacentes():
                indiceNuevo = self.ListaVertices.index(self.obtenervertice(vAdya))
                arista = self.obtenerarista(vAdya, aux.getDato())
                if caminos[indiceNuevo] > valorActual + arista.getPeso():
                    caminos[indiceNuevo] = valorActual + arista.getPeso()
                    VerticesAux[indiceNuevo] = self.ListaVertices[indice].getDato()
        return caminos

    def menorNoMarcado(self, caminos, marcados):
        verticeMenor = None
        caminosAux = sorted(caminos)
        copiacaminos = copy(caminos)
        bandera = True
        contador = 0
        while bandera:
            menor = caminosAux[contador]
            if marcados[copiacaminos.index(menor)] == False:
                verticeMenor = self.ListaVertices[copiacaminos.index(menor)]
                bandera = False
            else:
                copiacaminos[copiacaminos.index(menor)] = "x"
                contador = contador + 1
        return verticeMenor

    def todosMarcados(self, marcados):
        for j in marcados:
            if j is False:
                return False
        return True