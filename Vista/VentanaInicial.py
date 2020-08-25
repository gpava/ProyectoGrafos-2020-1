from tkinter import filedialog
from PIL import Image, ImageTk
import PIL.Image
import time
import json
import random
from playsound import playsound
from Proyecto20201.Vista.VentanaCueva import *
from Proyecto20201.Vista.VentanaGrado import *
from Proyecto20201.Vista.VentanaRuta import *
from Proyecto20201.Vista.VentanaDireccion import *
from Proyecto20201.Vista.VentanaCaminos import *
from Proyecto20201.Vista.InfoGrados import *
from Proyecto20201.Vista.InfoInaccesible import *
from Proyecto20201.Vista.InfoPozos import *
from Proyecto20201.Vista.InfoConexo import *
from Proyecto20201.Clases.Grafo import Grafo


class VentanaInicial:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Estructuras de Datos: Montaña Acme')
        self.ventana.geometry("1200x614")
        #self.ventana.resizable(0, 0)
        #self.ventana.config(bg="#4A7B0E")
        self.imagen = Image.open("../Imagenes/fondo.png")  # fondo
        imagen_de_fondo = ImageTk.PhotoImage(self.imagen)
        fondo = Label(self.ventana, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        #Cargo la imagen
        self.centrorecursos = PhotoImage(file="../Imagenes/centrorecursos.png")
        #Creo la etiqueta
        self.labelogo=Label(self.ventana, image=self.centrorecursos).place(x=10, y=10)
        #self.labelogo.grid(row=1,column=0)
        barraMenu = Menu(self.ventana)
        self.ventana.config(menu=barraMenu)
        self.sonidocamion = '../Datos/camion.mp3'

        archivoMenu = Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Cargar", command=self.cargar)
        archivoMenu.add_command(label="Reiniciar Aplicación", command=self.reiniciar)

        mostrarMenu = Menu(barraMenu, tearoff=0)
        mostrarMenu.add_command(label="Nueva Cueva", command=self.nuevacueva)
        mostrarMenu.add_command(label="Cambiar Direccion", command=self.cambiarsentido)

        iniciarMenu = Menu(barraMenu, tearoff=0)
        iniciarMenu.add_command(label="Fuerte o Debilmente Conexo", command=self.fdconexo)
        iniciarMenu.add_command(label="Pozos y fuentes", command=self.pozos)
        iniciarMenu.add_command(label="Conexiones Entrantes y Salientes por Cueva", command=self.gradovertices)

        obstruirMenu = Menu(barraMenu, tearoff=0)
        obstruirMenu.add_command(label="Bloquear", command=self.bloquearCamino)
        obstruirMenu.add_command(label="Desbloquear", command=self.desbloquearCamino)

        recorridoMenu = Menu(barraMenu, tearoff=0)
        recorridoMenu.add_command(label="Anchura", command=self.recorridoAnchura)
        recorridoMenu.add_command(label="Profundidad", command=self.recorridoprofundidad)
        recorridoMenu.add_command(label="Prim", command=self.recorridoPrim)
        recorridoMenu.add_command(label="Kruskal", command=self.recorridokruskal)
        recorridoMenu.add_command(label="Boruvka", command=self.recorridoboruvka)
        recorridoMenu.add_command(label="Ruta más corta", command=self.rutamascorta)

        barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
        barraMenu.add_cascade(label="Crear", menu=mostrarMenu)
        barraMenu.add_cascade(label="Información", menu=iniciarMenu)
        barraMenu.add_cascade(label="Obstruir", menu=obstruirMenu)
        barraMenu.add_cascade(label="Recorridos", menu=recorridoMenu)


        self.ventana.mainloop()  #lleva el registro de la ventana

    def cargar(self):
        global app
        app=Tk()
        app.withdraw()
        app.update()
        pahtString = filedialog.askopenfilename(filetypes=[("Text files", "*.json")])
        if pahtString != "":
            with open(pahtString, 'r') as content:
                self.infoJson = json.loads(content.read())
        self.canvas = Canvas(self.ventana, width=890, height=580, bg="#4A7B0E")
        self.canvas.place(x=260, y=10)

        self.reporteCanvas = Canvas(self.ventana, width=235, height=184,bg="#4A7B0E")
        self.reporteCanvas.place(x=22, y=210)
        Label(self.reporteCanvas, text="--Caminos Obstruidos--", font=("Verdana", 10), bg="#4A7B0E").pack(padx=10, pady=3)

        self.grafo = Grafo()
        self.crearGrafo()
        self.graficar()

    def reiniciar(self):
        self.canvas.destroy()
        self.reporteCanvas.destroy()

    def cambiarsentido(self):
        ventanasentido = VentanaDireccion(self.ventana)
        if ventanasentido.res:
            if self.grafo.verificararista(ventanasentido.origen, ventanasentido.destino):
                origenViejo = self.grafo.obtenervertice(ventanasentido.origen)
                destinoViejo = self.grafo.obtenervertice(ventanasentido.destino)
                origenNuevo = self.grafo.obtenervertice(ventanasentido.origen2)
                destinoNuevo = self.grafo.obtenervertice(ventanasentido.destino2)
                v = self.grafo.obtenerarista(origenViejo.getDato(), destinoViejo.getDato())
                self.grafo.eliminarArista(origenViejo.getDato(), destinoViejo.getDato())
                self.grafo.ingresararista(origenNuevo.getDato(), destinoNuevo.getDato(), v.getPeso(), True)
            else:
                messagebox.showwarning('Advertencia',
                'Los datos ingresados no son validos en''\nla base de información''\n\nVerifique los datos ingresados!')
        print("-------------------------------------")
        self.grafo.imprimiraristas()

    def nuevacueva(self):
        app = VentanaCueva(self.ventana)
        if app.res:
            x = random.randint(90, 830)
            y = random.randint(40, 600)
            coordenada = [x, y]
            if not self.grafo.verificarvertice(app.origen):
                self.grafo.ingresarvertice(app.origen, coordenada)
                if self.grafo.verificarvertice(app.origen2):
                    if app.origen3 == "si":
                        self.grafo.ingresararista(app.origen, app.origen2, int(app.origen4), True)
                        verticenuevo = self.grafo.obtenervertice(app.origen)
                        self.pintarnuevaconexion(app.origen, app.origen2, int(app.origen4))
                        self.pintarnuevacueva(verticenuevo)
                    elif app.origen3 == "no":
                        self.grafo.ingresararista(app.origen, app.origen2, int(app.origen4), False)
                        verticenuevo = self.grafo.obtenervertice(app.origen)
                        self.pintarnuevaconexion(app.origen, app.origen2, int(app.origen4))
                        self.pintarnuevacueva(verticenuevo)
                    else:
                        messagebox.showwarning('Advertencia',
                              'Los datos ingresados no son validos en''\nla base de información''\n\nVerifique los datos ingresados!')
            else:
                messagebox.showwarning('Advertencia',
                     'Los datos ingresados no son validos en''\nla base de información''\n\nVerifique los datos ingresados!')

    def fdconexo(self):
        p = self.grafo.numerodepozos()
        f = self.grafo.numerodefuentes()
        cadena = self.grafo.esfdconexo(p, f)
        InfoConexo(self.ventana, cadena)

    def pozos(self):
        self.grafo.setPozos(0)
        self.grafo.setFuentes(0)
        p = self.grafo.numerodepozos()
        f = self.grafo.numerodefuentes()
        InfoPozos(self.ventana, p,f)

    def gradovertices(self):
        ventanagrados = VentanaGrado(self.ventana)
        if ventanagrados.res:
            if self.grafo.verificarvertice(ventanagrados.origen):
                vertice = self.grafo.obtenervertice(ventanagrados.origen)
                conexionentrada = vertice.gradoentrada()
                conexionsalida = vertice.gradosalida()
                InfoGrados(self.ventana, vertice.getDato(), conexionentrada, conexionsalida)
            else:
                messagebox.showwarning('Advertencia',
                                       'Los datos ingresados no son validos en''\nla base de información''\n\nVerifique los datos ingresados!')

    def crearGrafo(self):
        for montana in self.infoJson.get("acme"):
            for cueva in montana.get("cuevas"):
                coordenates = []
                coordenates.append(cueva.get("coordenates").get("x"))
                coordenates.append(cueva.get("coordenates").get("y"))
                self.grafo.ingresarvertice(cueva.get("nombre"),coordenates)
        for montana in self.infoJson.get("acme"):
            for cueva in montana.get("cuevas"):
                for arista in cueva.get("conexion"):
                    self.grafo.ingresararista(cueva.get("nombre"), arista.get("nombre"), arista.get("peso"), False)

    def graficar(self):
        self.pintarconexiones()
        self.pintarCuevas()

    def pintarconexiones(self):
        for v in self.grafo.getListaAristas():
            self.pintarnuevaconexion(v.getOrigen(), v.getDestino(), v.getPeso())

    def pintarCuevas(self):
        for v in self.grafo.getListaVertices():
            self.pintarnuevacueva(v)

    def pintarnuevacueva(self,origen):
        coordenatesO = origen.getCoordenates()
        xO = coordenatesO[0]
        yO = coordenatesO[1]
        radio = 10
        self.canvas.create_text(xO, yO - 30, text=origen.getDato(), font=("Verdana", 12))
        self.canvas.create_rectangle(xO - radio, yO - radio, xO + radio, yO + radio, fill="#514e19")
        """imagen = tkinter.PhotoImage(file = "../Imagenes/cueva.png")
        self.canvas.create_image(xO - radio, yO - radio,
                                 image=imagen)"""

    def pintarnuevaconexion(self,origen,destino,peso):
        Vo = self.grafo.obtenervertice(origen)
        Vd = self.grafo.obtenervertice(destino)
        coordenatesO = Vo.getCoordenates()
        xO = coordenatesO[0]
        yO = coordenatesO[1]
        coordenatesD = Vd.getCoordenates()
        xD = coordenatesD[0]
        yD = coordenatesD[1]
        self.canvas.create_line(xO, yO, xD, yD, fill="orange", width=2.5)
        x = (xD - xO) / 2 + 13
        y = (yD - yO) / 2 + 13
        self.canvas.create_text(xO + x, yO + y, text=str(peso),font=("Verdana",13))

    def bloquearCamino(self):
        vc = VentanaRuta(self.ventana)
        if vc.res:
            if self.grafo.verificararista(vc.origen, vc.destino):
                verticeOrigen = self.grafo.obtenervertice(vc.origen)
                verticeDestino = self.grafo.obtenervertice(vc.destino)
                self.grafo.agregarBloqueada(verticeOrigen.getDato(), verticeDestino.getDato())
                self.grafo.eliminarArista(verticeOrigen.getDato(), verticeDestino.getDato())
                self.pintarCaminoBloqueado(verticeOrigen, verticeDestino)
                print(self.grafo.verificararista(verticeOrigen.getDato(), verticeDestino.getDato()))
                Label(self.reporteCanvas,
                text = "Obstruccion: " + verticeOrigen.getDato() + "\n" +" ---> " + verticeDestino.getDato(),
                                  font = ("Verdana", 10), bg="#4A7B0E").pack(padx=10, pady=1)
            else:
                messagebox.showwarning('Advertencia',
                     'Los datos ingresados no son ''\nvalidos, por favor ''\n\nVerifique los datos ingresados!')
        print("------------------")
        self.grafo.imprimiraristas()
        print("--------------------")
        for Arista in self.grafo.getListaBloqueados():
            print("Origen: {0} - Destino: {1} - Peso: {2}".format(Arista.getOrigen(), Arista.getDestino(),
                                                                  Arista.getPeso()))

    def pintarCaminoBloqueado(self, verticeOrigen, verticeDestino):
        coordenatesO = verticeOrigen.getCoordenates()
        xO = coordenatesO[0]
        yO = coordenatesO[1]
        coordenatesD = verticeDestino.getCoordenates()
        xD = coordenatesD[0]
        yD = coordenatesD[1]
        self.canvas.create_line(xO, yO, xD, yD, fill="red", width=2.5)

    def despintarCaminoBloqueado(self,verticeOrigen, verticeDestino):
        coordenatesO = verticeOrigen.getCoordenates()
        xO = coordenatesO[0]
        yO = coordenatesO[1]
        coordenatesD = verticeDestino.getCoordenates()
        xD = coordenatesD[0]
        yD = coordenatesD[1]
        self.canvas.create_line(xO, yO, xD, yD, fill="orange", width=2.5)

    def desbloquearCamino(self):
        vd = VentanaRuta(self.ventana)
        if vd.res:
            if self.grafo.verificararistabloqueada(vd.origen, vd.destino):
                verticeOrigen = self.grafo.obtenervertice(vd.origen)
                verticeDestino = self.grafo.obtenervertice(vd.destino)
                self.grafo.desbloqueararista(verticeOrigen.getDato(), verticeDestino.getDato())
                print(self.grafo.verificararista(verticeOrigen.getDato(), verticeDestino.getDato()))
                self.despintarCaminoBloqueado(verticeOrigen, verticeDestino)
                Label(self.reporteCanvas,
                      text="Desbloqueado: " + verticeOrigen.getDato() + "\n"+" --> " + verticeDestino.getDato(),
                      font=("Verdana", 10), bg="#4A7B0E").pack(padx=10, pady=1)
            else:
                messagebox.showwarning('Advertencia',
                        'Los datos ingresados no son''\nvalidos, por favor ''\n\nVerifique los datos ingresados!')
        """print("------------------")
        self.grafo.imprimiraristas()
        print("--------------------")
        for Arista in self.grafo.getListaBloqueados():
            print("Origen: {0} - Destino: {1} - Peso: {2}".format(Arista.getOrigen(), Arista.getDestino(),
                                                                  Arista.getPeso()))"""

    def recorridoAnchura(self):
        anchu = VentanaCaminos(self.ventana)
        if anchu.res:
            self.recorridoanchuraCuevas(anchu.origen)

    def recorridoanchuraCuevas(self,dato):
        if self.grafo.verificarvertice(dato):
            self.listaanchura = self.grafo.amplitud(dato)
            self.grafo.setFuentes(0)
            self.grafo.setListaFuentes([])
            self.grafo.fuentesgrafo()
            self.grafo.inaccesible(self.grafo.getListaFuentes())
            self.pintarrecorrido(self.listaanchura)
            if self.grafo.getListaFuentes():
                InfoInaccesible(self.ventana, self.grafo.getListaFuentes(), self.grafo.getListaBloqueados())
        else:
            messagebox.showwarning('Advertencia',
                             'Los datos ingresados no se encuentran en''\nla base de información''\n\nVerifique los datos ingresados!')

    def pintarrecorrido(self, listaRecorrido):
        for cont in range(len(listaRecorrido) - 1):
            #time.sleep(1)
            o=self.grafo.obtenervertice(listaRecorrido[cont])
            coordenatesO = o.getCoordenates()
            xO = coordenatesO[0]
            yO = coordenatesO[1]
            d = self.grafo.obtenervertice(listaRecorrido[cont + 1])
            coordenatesD = d.getCoordenates()
            xD = coordenatesD[0]
            yD = coordenatesD[1]
            self.canvas.create_line(xO, yO, xD, yD, fill="#3b41aa", width=2.5)
            self.pintarCamion(o)
            self.pintarCamion(d)
            playsound(self.sonidocamion)
            self.canvas.update()
        time.sleep(2)

    def pintarCamion(self, vertice):
        imagen = PIL.Image.open('../Imagenes/Camion.png')
        imagen.thumbnail((75, 75), PIL.Image.ANTIALIAS)
        self.camionImagen = ImageTk.PhotoImage(imagen)
        radio = 10
        coordenadas = vertice.getCoordenates()
        self.canvas.create_image(coordenadas[0] - radio, coordenadas[1] - radio, anchor=NW,
                                 image=self.camionImagen)

    def recorridoprofundidad(self):
        prof = VentanaCaminos(self.ventana)
        if prof.res:
            self.recorridoprofundidadCuevas(prof.origen)

    def rutamascorta(self):
        self.grafo.setFuentes(0)
        self.grafo.setListaFuentes([])
        self.grafo.fuentesgrafo()
        self.grafo.inaccesible(self.grafo.getListaFuentes())
        #si hay fuentes ir a dijsktra dirigido
        if self.grafo.getListaFuentes():
            InfoInaccesible(self.ventana, self.grafo.getListaFuentes(), self.grafo.getListaBloqueados())
        #ventana de la ruta mas corta
        venta = VentanaRuta(self.ventana)
        if venta.res:
            if self.grafo.verificarvertice(venta.origen) and self.grafo.verificarvertice(venta.destino):
                dorigen = self.grafo.obtenervertice(venta.origen)
                ddestino = self.grafo.obtenervertice(venta.destino)
                listauxiliar = self.grafo.caminoMasCorto(dorigen.getDato(), ddestino.getDato())
                self.pintarrecorrido(listauxiliar)
            else:
                messagebox.showwarning('Advertencia',
                                        'Los datos ingresados no se encuentran en''\nla base de información''\n\nVerifique los datos ingresados!')

    def recorridoprofundidadCuevas(self,dato):
        if self.grafo.verificarvertice(dato):
            self.grafo.profundidad(dato)
            self.grafo.setFuentes(0)
            self.grafo.setListaFuentes([])
            self.grafo.fuentesgrafo()
            self.grafo.inaccesible(self.grafo.getListaFuentes())
            self.pintarrecorrido(self.grafo.getListaVisitados())
            if self.grafo.getListaFuentes():
                InfoInaccesible(self.ventana, self.grafo.getListaFuentes(), self.grafo.getListaBloqueados())
        else:
            messagebox.showwarning('Advertencia',
                         'Los datos ingresados no se encuentran en''\nla base de información''\n\nVerifique los datos ingresados!')

    """def recorridoPrim(self):
        prim = VentanaCaminos(self.ventana)
        if prim.res:
            self.recorridoPrimCuevas(prim.origen)
            
    def recorridoPrimCuevas(self,dato):
        if self.grafo.verificarvertice(dato):
            self.grafo.setFuentes(0)
            self.grafo.setListaFuentes([])
            self.grafo.fuentesgrafo()
            self.grafo.inaccesible(self.grafo.getListaFuentes())
            self.pintarrecorridominimo(self.grafo.Prim(dato))
            if self.grafo.getListaFuentes():
                InfoInaccesible(self.ventana, self.grafo.getListaFuentes(), self.grafo.getListaBloqueados())"""

    def recorridoPrim(self):
        self.grafo.setFuentes(0)
        self.grafo.setListaFuentes([])
        self.grafo.fuentesgrafo()
        self.grafo.inaccesible(self.grafo.getListaFuentes())
        self.pintarrecorridominimo(self.grafo.arbolPrim())
        if self.grafo.getListaFuentes():
            InfoInaccesible(self.ventana, self.grafo.getListaFuentes(), self.grafo.getListaBloqueados())

    def recorridokruskal(self):
        self.grafo.setFuentes(0)
        self.grafo.setListaFuentes([])
        self.grafo.fuentesgrafo()
        self.grafo.inaccesible(self.grafo.getListaFuentes())
        self.pintarrecorridominimo(self.grafo.Kruskal())
        if self.grafo.getListaFuentes():
            InfoInaccesible(self.ventana, self.grafo.getListaFuentes(),self.grafo.getListaBloqueados())

    def recorridoboruvka(self):
        self.grafo.setFuentes(0)
        self.grafo.setListaFuentes([])
        self.grafo.fuentesgrafo()
        self.grafo.inaccesible(self.grafo.getListaFuentes())
        self.pintarrecorridominimo(self.grafo.Boruvka())
        if self.grafo.getListaFuentes():
            InfoInaccesible(self.ventana, self.grafo.getListaFuentes(),self.grafo.getListaBloqueados())

    def pintarrecorridominimo(self, listaAristas):
        for arista in listaAristas:
            time.sleep(1)
            o=self.grafo.obtenervertice(arista.getOrigen())
            coordenatesO = o.getCoordenates()
            xO = coordenatesO[0]
            yO = coordenatesO[1]
            d = self.grafo.obtenervertice(arista.getDestino())
            coordenatesD = d.getCoordenates()
            xD = coordenatesD[0]
            yD = coordenatesD[1]
            self.canvas.create_line(xO, yO, xD, yD, fill="#cee5e2", width=2.5)
            self.pintarCamion(o)
            self.pintarCamion(d)
            playsound(self.sonidocamion)
            self.canvas.update()
        time.sleep(2)


VentanaInicial()