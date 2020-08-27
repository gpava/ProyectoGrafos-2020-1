from tkinter import *
from PIL import Image, ImageTk

class InfoConexo():

    def __init__(self, app,mensaje):
        self.t1 = Toplevel(app) #"ventana secundaria" de dialogo
        self.t1.geometry('380x200')
        self.t1.title("Número de Pozo de la Montaña Acme")
        self.imagen = Image.open("../Imagenes/fondo3.png")  # fondo
        imagen_de_fondo = ImageTk.PhotoImage(self.imagen)
        fondo = Label(self.t1, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1.focus_set()
        self.t1.resizable(0, 0)
        self.t1.grab_set()
        self.t1.transient(master=app) #ventana transitoria se dibuja encima del padre app

        Label(self.t1,
                  text=mensaje, font=("Verdana", 13)).pack(padx=10, pady=10)

        self.t1.wait_window(self.t1) #espera a que esta se cierra para seguir con otra acción