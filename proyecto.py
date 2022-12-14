from tkinter import *
from tkinter import messagebox


class MenuPrincipal:
    def __init__(self) -> None:
        self.ventana=Tk()
        self.ventana.title("Domicilios Uninorte")
        self.ventana.iconbitmap("domicilios_uninorte.ico")
        self.frameven=Frame(self.ventana)
        self.frameven.pack()
        self.ventana.resizable(False,False)

        titulo =Label(self.frameven, text="¬°DOMICILIOS UNINORTE!", font=("Times New Roman",15))
        titulo.grid(row=0, column=1, padx=10, pady=10)
        
        subtitulo =Label(self.frameven, text="En Domicilios Uninorte puedes:", font=("Times New Roman",12))
        subtitulo.grid(row=1, column=0, padx=10, pady=10)

        def salir():
            self.ventana.destroy()
            messagebox.showinfo(message="Gracias por utilizar nuestra App, hasta luego.", title="Hasta Luego")

        botonsalir= Button(self.frameven, text="Salir", command=salir)
        botonsalir.grid(row=4, column=2, padx=10, pady=10)

        def alquiler():
            self.ventana.destroy()
            AlquilerProducto()

        alquilerLabel=Label(self.frameven, text="Alquiler de articulos: ")
        alquilerLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        botonConfirmar2= Button(self.frameven, text="Alquilar", command=alquiler)
        botonConfirmar2.grid(row=2, column=1, padx=10, pady=10)

        def comprar():
            self.ventana.destroy()
            CompraProducto()

        alquilerLabel=Label(self.frameven, text="Compra en establecimiento Dunord: ")
        alquilerLabel.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        botonConfirmar2= Button(self.frameven, text="Comprar", command=comprar)
        botonConfirmar2.grid(row=3, column=1, padx=10, pady=10)

        self.ventana.mainloop()

class AlquilerProducto:
    def __init__(self) -> None:
        self.ventana_a=Tk()
        self.ventana_a.title("Domicilios Uninorte")
        self.ventana_a.iconbitmap("domicilios_uninorte.ico")
        self.frameven=Frame(self.ventana_a)
        self.frameven.pack()
        self.ventana_a.resizable(False,False)

        titulo =Label(self.frameven, text="¬°DOMICILIOS UNINORTE!", font=("Times New Roman",15))
        titulo.grid(row=0, column=0, padx=10, pady=10)

        subtitulo =Label(self.frameven, text="Para articulos de alquiler se\nencuentran disponibles:", font=("Times New Roman", 12))
        subtitulo.grid(row=1, column=0, padx=10, pady=10)

        def alquiler():
            self.ventana_a.destroy()
            messagebox.showinfo(message="Su pedido fue realizado correctamente, pronto estar√° en camino.", title="Correcto")

        botonConfirm1= Button(self.frameven, text="Alquilar", command=alquiler)
        botonConfirm1.grid(row=4, column=1, padx=10, pady=10)

        computador=IntVar()
        guitarra=IntVar()
        marcadores=IntVar()
        calculadora=IntVar()
        raquetadetenis=IntVar()

        def opcionesalquiler():
            opcionesElegida=""

            if (computador.get()==1):
                opcionesElegida+="Computador "
            if (guitarra.get()==1):
                opcionesElegida+="Guitarra "
            if (marcadores.get()==1):
                opcionesElegida+="Marcadores "
            if (calculadora.get()==1):
                opcionesElegida+="Calculadora "
            if (raquetadetenis.get()==1):
                opcionesElegida+="Raqueta de Tenis "
            
            textoMostrado.config(text="Los articulos elegidos son:\n" + opcionesElegida)   
        
        def precio():
            precio_final=0

            if (computador.get()==1):
                precio_final+=2000
            if (guitarra.get()==1):
                precio_final+=1500
            if (marcadores.get()==1):
                precio_final+=500
            if (calculadora.get()==1):
                precio_final+=1000
            if (raquetadetenis.get()==1):
                precio_final+=1200

            textoMostradoprecio.config(text="El precio a pagar es: " + str(precio_final))

        Checkbutton(self.frameven, text="Computador", variable= computador, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 2, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Guitarra", variable= guitarra, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 3, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Marcadores", variable= marcadores, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 4, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Calculadora", variable= calculadora, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 5, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Raqueta de Tenis", variable= raquetadetenis, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 6, column=0, padx=10, pady=10, sticky="e")

        textoMostrado=Label(self.frameven)
        textoMostrado.grid(row=7, column=0)

        textoMostradoprecio=Label(self.frameven)
        textoMostradoprecio.grid(row=5, column=1)

        

        def regresar():
            self.ventana_a.destroy()
            MenuPrincipal()

        botonRegresar1= Button(self.frameven, text="Regresar", command=regresar)
        botonRegresar1.grid(row=7, column=1, padx=10, pady=10)

        self.ventana_a.mainloop()

class CompraProducto:
    def __init__(self) -> None:
        self.ventana_b=Tk()
        self.ventana_b.title("Domicilios Uninorte")
        self.ventana_b.iconbitmap("domicilios_uninorte.ico")
        self.frameven=Frame(self.ventana_b)
        self.frameven.pack()
        self.ventana_b.resizable(False,False)
        
        titulo =Label(self.frameven, text="¬°DOMICILIOS UNINORTE!", font=("Times New Roman",15))
        titulo.grid(row=0, column=1, padx=10, pady=10)

        subtitulo =Label(self.frameven, text="Los establecimientos que se\nencuentran disponibles con\n sus distintos productos son:", font=("Times New Roman",12))
        subtitulo.grid(row=1, column=0, padx=10, pady=10)

        def comprar():
            self.ventana_b.destroy()
            messagebox.showinfo(message="Su pedido fue realizado correctamente, pronto estar√° en camino.", title="Correcto")

        botonConfirm2= Button(self.frameven, text="Comprar", command=comprar)
        botonConfirm2.grid(row=6, column=3, padx=10, pady=10)

        dedito=IntVar()
        perro=IntVar()
        salchipapa=IntVar()
        mazorca=IntVar()

        galleta=IntVar()
        brownie=IntVar()
        sandwich=IntVar()
        cockiepie=IntVar()

        pastas=IntVar()
        paletas=IntVar()
        colombinas=IntVar()
        nuggets=IntVar()

        choclitos=IntVar()
        takis=IntVar()
        detodito=IntVar()
        gomitas=IntVar()

        def opcionesalquiler():
            opcionesElegida=""

            if (dedito.get()==1):
                opcionesElegida+="Dedito "
            if (perro.get()==1):
                opcionesElegida+="Perro Caliente "
            if (salchipapa.get()==1):
                opcionesElegida+="Salchipapa "
            if (mazorca.get()==1):
                opcionesElegida+="Mazorca Desgranada "

            if (galleta.get()==1):
                opcionesElegida+="Galleta "
            if (brownie.get()==1):
                opcionesElegida+="Brownie "
            if (sandwich.get()==1):
                opcionesElegida+="Sandwich "
            if (cockiepie.get()==1):
                opcionesElegida+="Cockie Pie "

            if (pastas.get()==1):
                opcionesElegida+="Pastas "
            if (paletas.get()==1):
                opcionesElegida+="Paletas "
            if (colombinas.get()==1):
                opcionesElegida+="Colombinas de Pollo "
            if (nuggets.get()==1):
                opcionesElegida+="Nuggets de Pollo "

            if (choclitos.get()==1):
                opcionesElegida+="Choclitos "
            if (takis.get()==1):
                opcionesElegida+="Takis Fuego "
            if (detodito.get()==1):
                opcionesElegida+="Detodito BBQ "
            if (gomitas.get()==1):
                opcionesElegida+="Gomitas ORO"

            textoMostrado.config(text="Los articulos elegidos son:\n" + opcionesElegida)   

        def precio():
            precio_final=0

            if (dedito.get()==1):
                precio_final+=2900
            if (perro.get()==1):
                precio_final+=4500
            if (salchipapa.get()==1):
                precio_final+=10000
            if (mazorca.get()==1):
                precio_final+=11500

            if (galleta.get()==1):
                precio_final+=3900
            if (brownie.get()==1):
                precio_final+=3500
            if (sandwich.get()==1):
                precio_final+=12500
            if (cockiepie.get()==1):
                precio_final+=18500

            if (pastas.get()==1):
                precio_final+=16500
            if (paletas.get()==1):
                precio_final+=7900
            if (colombinas.get()==1):
                precio_final+=16900
            if (nuggets.get()==1):
                precio_final+=17900

            if (choclitos.get()==1):
                precio_final+=7700
            if (takis.get()==1):
                precio_final+=3200
            if (detodito.get()==1):
                precio_final+=7000
            if (gomitas.get()==1):
                precio_final+=2900

            textoMostradoprecio.config(text="El precio a pagar es:\n" + str(precio_final))

        expressLabel=Label(self.frameven, text="DuNord Express: ", font=("Times New Roman", 10))
        expressLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        Checkbutton(self.frameven, text="Dedito", variable= dedito, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 3, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Perro Caliente", variable= perro, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 4, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Salchipapa", variable= salchipapa, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 5, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Mazorca Desgranada", variable= mazorca, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 6, column=0, padx=10, pady=10, sticky="e")
        
        terrasseLabel=Label(self.frameven, text="DuNord Terrasse: ", font=("Times New Roman", 10))
        terrasseLabel.grid(row=7, column=0, padx=10, pady=10, sticky="e")

        Checkbutton(self.frameven, text="Galleta", variable= galleta, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 8, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Brownie", variable= brownie, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 9, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Sandwich", variable= sandwich, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 10, column=0, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Cockie Pie", variable= cockiepie, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 11, column=0, padx=10, pady=10, sticky="e")

        cafeLabel=Label(self.frameven, text="DuNord Cafe: ", font=("Times New Roman", 10))
        cafeLabel.grid(row=2, column=2, padx=10, pady=10, sticky="e")

        Checkbutton(self.frameven, text="Pastas", variable= pastas, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 3, column=2, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Paletas", variable= paletas, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 4, column=2, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Colombinas de Pollo", variable= colombinas, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 5, column=2, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Nuggets de Pollo", variable= nuggets, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 6, column=2, padx=10, pady=10, sticky="e")


        storeLabel=Label(self.frameven, text="DuNord Store: ", font=("Times New Roman", 10))
        storeLabel.grid(row=7, column=2, padx=10, pady=10, sticky="e")

        Checkbutton(self.frameven, text="Choclitos", variable= choclitos, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 8, column=2, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Takis Fuego", variable= takis, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 9, column=2, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Detodito BBQ", variable= detodito, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 10, column=2, padx=10, pady=10, sticky="e")
        Checkbutton(self.frameven, text="Gomitas ORO", variable= gomitas, onvalue=1, offvalue=0, command=opcionesalquiler and precio).grid(row= 11, column=2, padx=10, pady=10, sticky="e")

        textoMostrado=Label(self.frameven)
        textoMostrado.grid(row=12, column=0)

        textoMostradoprecio=Label(self.frameven)
        textoMostradoprecio.grid(row=7, column=3)

        def regresar():
            self.ventana_b.destroy()
            MenuPrincipal()

        botonRegresar2= Button(self.frameven, text="Regresar", command=regresar)
        botonRegresar2.grid(row=12, column=3, padx=10, pady=10)

        self.ventana_b.mainloop()

class GUI_Usuario:
    
    def __init__(self) -> None:

        self.raiz=Tk()
        self.raiz.resizable(False, False)
        self.raiz.title("Domicilios Uninorte")
        self.raiz.iconbitmap("domicilios_uninorte.ico")
        self.frame1= Frame(self.raiz)
        self.frame1.pack()
    
        titulo =Label(self.frame1, text="¬°DOMICILIOS UNINORTE! \n Login:", font=("Times New Roman",15))
        titulo.grid(row=0, column=1, padx=10, pady=10)

        usuario=StringVar()
        self.cuadroUsuario=Entry(self.frame1, textvariable=usuario)
        self.cuadroUsuario.grid(row=1, column=1, padx=10, pady=10)
        usuarioLabel=Label(self.frame1, text="Usuario: ")
        usuarioLabel.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        contra=StringVar()
        self.cuadroContrasena=Entry(self.frame1, textvariable=contra)
        self.cuadroContrasena.grid(row=2, column=1, padx=10, pady=10)
        self.cuadroContrasena.config(show="‚ÄĘ")
        contrasenaLabel=Label(self.frame1, text="Contrase√Īa: ")
        contrasenaLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        def ingresar():
            if usuario.get()=="usuario1" and contra.get()=="contra1" :
                self.raiz.destroy()
            else:
                messagebox.showerror(message="Incorrecto, por favor intente de nuevo.", title="Incorrecto")
                messagebox.showinfo(message="El usuario es: usuario1 - La contrase√Īa es: contra1", title="Informaci√≥n importante")


        botonConfirmar= Button(self.frame1, text="Confirmar", command=ingresar)
        botonConfirmar.grid(row=3, column=1, padx=10, pady=10)

        self.raiz.mainloop()