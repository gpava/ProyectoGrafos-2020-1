from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class VentanaDireccion():

    def __init__(self, app):
        self.res = False
        self.t1 = Toplevel(app)
        self.t1.geometry('400x500')
        self.t1.title('Cambiar Direccion')
        self.imagen = Image.open("../Imagenes/fondo1.png")  # fondo
        imagen_de_fondo = ImageTk.PhotoImage(self.imagen)
        fondo = Label(self.t1, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1.focus_set()
        self.t1.resizable(0,0)
        self.t1.grab_set()
        self.t1.transient(master=app)


        Label(self.t1, text="Ingrese los Datos de la direccion a Cambiar",font=("Verdana",13)).pack(padx=10, pady=10)

        Label(self.t1, text="Ingrese la Cueva de Origen Vieja",font=("Verdana",13)).pack(padx=10, pady=10)

        self.vertex = ""
        self.origen = Entry(self.t1, textvariable=self.vertex)
        self.origen.pack(padx=15, pady=15)

        Label(self.t1, text="Ingrese la Cueva Destino Vieja",font=("Verdana",13)).pack(padx=10, pady=10)

        self.vertex2 = ""
        self.destino = Entry(self.t1, textvariable=self.vertex2)
        self.destino.pack(padx=15, pady=15)

        Label(self.t1, text="Ingrese la Cueva de Origen Nueva", font=("Verdana", 13)).pack(padx=10, pady=10)

        self.vertex3 = ""
        self.origen2 = Entry(self.t1, textvariable=self.vertex3)
        self.origen2.pack(padx=15, pady=15)

        Label(self.t1, text="Ingrese la Cueva Destino Nueva", font=("Verdana", 13)).pack(padx=10, pady=10)

        self.vertex4 = ""
        self.destino2 = Entry(self.t1, textvariable=self.vertex4)
        self.destino2.pack(padx=15, pady=15)

        Button(self.t1, text='Enviar', command=self.verificacion,bg="#4fed44",font=("Verdana",12)).pack(padx=10, pady=10)

        self.t1.wait_window(self.t1)

    def verificacion(self):
        try:
            origen = self.origen.get()
            destino = self.destino.get()
            origen2 = self.origen2.get()
            destino2 = self.destino2.get()
            self.origen2 = origen2
            self.destino2 = destino2
            self.origen = origen
            self.destino = destino
            self.res = True
            self.t1.destroy()
        except:
            messagebox.showwarning('Advertencia', '\nNo se han ingresado los datos \nIngreselos de nuevo')