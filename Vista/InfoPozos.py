from tkinter import *
from PIL import Image, ImageTk

class InfoPozos():

    def __init__(self, app,p,f):
        self.t1 = Toplevel(app)
        self.t1.geometry('380x200')
        self.t1.title("Número de Pozo de la Montaña Acme")
        self.imagen = Image.open("../Imagenes/fondo3.png")  # fondo
        imagen_de_fondo = ImageTk.PhotoImage(self.imagen)
        fondo = Label(self.t1, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1.focus_set()
        self.t1.resizable(0, 0)
        self.t1.grab_set()
        self.t1.transient(master=app)

        if p != 0:
            Label(self.t1,
                  text="La Montaña Acme tiene: " + "\n" + str(p) + " Pozos", font=("Verdana", 14)).pack(padx=10,
                                                                                                        pady=10)
        else:
            Label(self.t1,
                  text="La Montaña Acme No tiene Pozos", font=("Verdana", 14)).pack(padx=10, pady=10)

        if f != 0:
            Label(self.t1,
                  text="La Montaña Acme tiene: " + "\n" + str(f) + " Fuentes", font=("Verdana", 14)).pack(padx=10,
                                                                                                        pady=10)
        else:
            Label(self.t1,
                  text="La Montaña Acme No tiene fuentes", font=("Verdana", 14)).pack(padx=10, pady=10)

        self.t1.wait_window(self.t1)