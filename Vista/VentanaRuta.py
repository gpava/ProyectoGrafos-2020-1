from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class VentanaRuta:

    def __init__(self, app):
        self.res = False
        self.t1 = Toplevel(app)
        self.t1.geometry('400x400')
        self.t1.title('Ingrese la Ruta')
        self.imagen = Image.open("../Imagenes/fondo3.png")  # fondo
        imagen_de_fondo = ImageTk.PhotoImage(self.imagen)
        fondo = Label(self.t1, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1.focus_set()
        self.t1.resizable(0,0)
        self.t1.grab_set()
        self.t1.transient(master=app)

        Label(self.t1, text="Ingrese la Cueva de Origen",font=("Verdana",13)).pack(padx=10, pady=10)

        self.vertex = ""
        self.origen = Entry(self.t1, textvariable=self.vertex)
        self.origen.pack(padx=15, pady=15)

        Label(self.t1, text="Ingrese la Cueva Destino",font=("Verdana",13)).pack(padx=10, pady=10)

        self.vertex2 = ""
        self.destino = Entry(self.t1, textvariable=self.vertex2)
        self.destino.pack(padx=15, pady=15)

        Button(self.t1, text='Enviar', command=self.verificacion,bg="#4fed44",font=("Verdana",12)).pack(padx=10, pady=10)

        self.t1.wait_window(self.t1)

    def verificacion(self):
        try:
            origen = self.origen.get()
            destino = self.destino.get()
            self.origen = origen
            self.destino = destino
            self.res = True
            self.t1.destroy()
        except:
            messagebox.showwarning('Advertencia', '\nNo se han ingresado los datos \nIngreselos de nuevo')