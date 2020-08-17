from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class VentanaCueva():

    def __init__(self, app):
        self.res = False
        self.t1 = Toplevel(app)
        self.t1.geometry('400x500')
        self.t1.title('Crear Cueva')
        self.imagen = Image.open("../Imagenes/fondo1.png")  #fondo
        imagen_de_fondo = ImageTk.PhotoImage(self.imagen)
        fondo = Label(self.t1, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1.focus_set()
        self.t1.resizable(0,0)
        self.t1.grab_set()
        self.t1.transient(master=app)
        Label(self.t1, text="Ingrese Nombre de la Cueva",font=("Verdana",13)).pack(padx=10, pady=10)

        self.vertex = ""
        self.origen = Entry(self.t1, textvariable=self.vertex)
        self.origen.pack(padx=15, pady=15)

        Label(self.t1, text="Ingrese el Destino de la Cueva",font=("Verdana",13)).pack(padx=10, pady=10)

        self.vertex2 = ""
        self.origen2 = Entry(self.t1, textvariable=self.vertex2)
        self.origen2.pack(padx=15, pady=15)

        Label(self.t1, text="Digite""\n"+" -Si- para Camino Dirigido"+"\n"+"-No- para Camino No Dirigido",font=("Verdana",13)).pack(padx=10, pady=10)

        self.vertex3 = ""
        self.origen3 = Entry(self.t1, textvariable=self.vertex3)
        self.origen3.pack(padx=15, pady=15)

        Label(self.t1, text="Digite la Distancia entre las Cuevas",font=("Verdana",13)).pack(padx=10, pady=10)

        self.vertex4 = ""
        self.origen4 = Entry(self.t1, textvariable=self.vertex4)
        self.origen4.pack(padx=15, pady=15)

        Button(self.t1, text='Enviar', command=self.verificacion,bg="#4fed44",font=("Verdana",12)).pack(padx=10, pady=10)

        self.t1.wait_window(self.t1)

    def verificacion(self):
        try:
            origen = self.origen.get()
            origen2 = self.origen2.get()
            origen3 = self.origen3.get()
            origen4 = self.origen4.get()
            self.origen = origen
            self.origen2 = origen2
            self.origen3 = origen3
            self.origen4 = origen4
            self.res = True
            self.t1.destroy()
        except:
            messagebox.showwarning('Advertencia', '\nLos datos ingresados son incorrectos \nIngreselos de nuevo')
