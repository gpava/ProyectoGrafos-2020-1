from tkinter import *
from PIL import Image, ImageTk

class InfoGrados():

    def __init__(self, app,dato,conexionentrante,conexionsaliente):
        self.t1 = Toplevel(app)
        self.t1.geometry('375x207')
        self.t1.title('Conexiones Entrantes y Salientes de '+dato)
        self.imagen = Image.open("../Imagenes/fondo2.png")  # fondo
        imagen_de_fondo = ImageTk.PhotoImage(self.imagen)
        fondo = Label(self.t1, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1.focus_set()
        self.t1.resizable(0,0)
        self.t1.grab_set()
        self.t1.transient(master=app)

        Label(self.t1, text="Conexiones Entrantes y Salientes "+"\n"+ "Conexiones entrantes"+"\n"+" de la Cueva " + dato
                                +"\n" +"\n"+"Conexiones Entrantes: " + str(conexionentrante) + "\n" + "\n"
                                    + "Conexiones Salientes: " + str(conexionsaliente), font=("Verdana", 13)).pack(padx=10, pady=10)

        self.t1.wait_window(self.t1)
