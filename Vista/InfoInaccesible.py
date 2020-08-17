from tkinter import *
from PIL import Image, ImageTk

class InfoInaccesible():

    def __init__(self, app,listafuentes):
        self.t1 = Toplevel(app)
        self.t1.geometry('666x496')
        self.t1.title("Caminos Inaccesibles")
        self.imagen = Image.open("../Imagenes/fondo3.png")  # fondo
        imagen_de_fondo = ImageTk.PhotoImage(self.imagen)
        fondo = Label(self.t1, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1.focus_set()
        self.t1.resizable(0, 0)
        self.t1.grab_set()
        self.t1.transient(master=app)

        Label(self.t1,
              text="Las Cuevas Inaccesibles son ", font=("Verdana", 9)).pack(padx=10, pady=10)

        for i in listafuentes:
            Label(self.t1,
                  text=i.getDato(), font=("Verdana", 9)).pack(padx=10, pady=10)
            Label(self.t1,
                  text="Se Recomienda Conectar a "+"\n"+i.getDato()+"\n"+"Con", font=("Verdana", 9)).pack(padx=10, pady=10)
            for j in i.getListaAdyacentes():
              Label(self.t1,text=j.getDato(),font=("Verdana", 9)).pack(padx=10, pady=10)

        self.t1.wait_window(self.t1)