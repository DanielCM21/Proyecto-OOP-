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

        titulo =Label(self.frameven, text="¡DOMICILIOS UNINORTE!", font=("Times New Roman",15))
        titulo.grid(row=0, column=1, padx=10, pady=10)
        
        titulo =Label(self.frameven, text="En Domicilios Uninorte puedes:", font=("Times New Roman",12))
        titulo.grid(row=1, column=0, padx=10, pady=10)

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

        def regresar():
            self.ventana_a.destroy()
            MenuPrincipal()

        botonRegresar1= Button(self.frameven, text="Regresar", command=regresar)
        botonRegresar1.grid(row=2, column=1, padx=10, pady=10)

        self.ventana_a.mainloop()

class CompraProducto:
    def __init__(self) -> None:
        self.ventana_b=Tk()
        self.ventana_b.title("Domicilios Uninorte")
        self.ventana_b.iconbitmap("domicilios_uninorte.ico")
        self.frameven=Frame(self.ventana_b)
        self.frameven.pack()
        self.ventana_b.resizable(False,False)

        def regresar():
            self.ventana_b.destroy()
            MenuPrincipal()

        botonRegresar2= Button(self.frameven, text="Regresar", command=regresar)
        botonRegresar2.grid(row=2, column=1, padx=10, pady=10)

        self.ventana_b.mainloop()
        
class GUI_Usuario:
    
    def __init__(self) -> None:

        self.raiz=Tk()
        self.raiz.resizable(False, False)
        self.raiz.title("Domicilios Uninorte")
        self.raiz.iconbitmap("domicilios_uninorte.ico")
        self.frame1= Frame(self.raiz)
        self.frame1.pack()
    
        titulo =Label(self.frame1, text="¡DOMICILIOS UNINORTE! \n Login:", font=("Times New Roman",15))
        titulo.grid(row=0, column=1, padx=10, pady=10)

        usuario=StringVar()
        self.cuadroUsuario=Entry(self.frame1, textvariable=usuario)
        self.cuadroUsuario.grid(row=1, column=1, padx=10, pady=10)
        usuarioLabel=Label(self.frame1, text="Usuario: ")
        usuarioLabel.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        contra=StringVar()
        self.cuadroContrasena=Entry(self.frame1, textvariable=contra)
        self.cuadroContrasena.grid(row=2, column=1, padx=10, pady=10)
        self.cuadroContrasena.config(show="•")
        contrasenaLabel=Label(self.frame1, text="Contraseña: ")
        contrasenaLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        def ingresar():
            if usuario.get()=="usuario1" and contra.get()=="contra1" :
                self.raiz.destroy()
                MenuPrincipal()
            else:
                messagebox.showerror(message="Incorrecto, por favor intente de nuevo.", title="Incorrecto")
                messagebox.showinfo(message="El usuario es: usuario1 - La contraseña es: contra1", title="Información importante")


        botonConfirmar= Button(self.frame1, text="Confirmar", command=ingresar)
        botonConfirmar.grid(row=3, column=1, padx=10, pady=10)

        self.raiz.mainloop()






class Pedidos_compra:
    def __init__(self, restaurante) -> None:
        self.dinero = 0
        self.restaurante = restaurante

    def seleccionar_producto(self):
        
        for i in self.restaurante:
            print(i + ". " + self.restaurante[i][0] + " tiene un precio de: " + str(self.restaurante[i][1]))
        restaurante = str(input("Digite cual es el producto que desea pedir: "))
        print("")
        print("Señor cliente usted ha ordenado: " + str(self.restaurante[restaurante][0]) + " el cual tiene un precio de $" + str(self.restaurante[restaurante][1]))
        print("")
        billete = input("Ingrese de cuanto es el billete con el que desea pagar: ")
        self.cambio(int(self.restaurante[restaurante][1]), int(billete))

    def cambio(self, costo, billete):
        self.dinero = int(billete) - int(costo)
        print("")
        print("El cambio es de: " + str(self.dinero))
        print("Muchas gracias por su compra, el pedido le llegará pronto.")

class Pedidos_alquiler:
    def __init__(self, alquiler) -> None:
        self.alquiler = alquiler
        self.dinero = 0

    def alquiler_articulo (self):

        for i in self.alquiler:
            print(i + ". " + self.alquiler[i][0] + " tiene un precio de deposito de: " + str(self.alquiler[i][1]))
        alquiler = str(input("Digite cual es el producto que desea alquilar: "))
        print("")
        print("Señor cliente usted ha ordenado para alquilar: " + str(self.alquiler[alquiler][0]) + " el cual tiene un deposito de $" + str(self.alquiler[alquiler][1]))
        print("")
        billete = input("Ingrese de cuanto es el billete con el que desea pagar: ")
        self.cambio(int(self.alquiler[alquiler][1]), int(billete))

    def cambio(self, costo, billete):
        self.dinero = int(billete) - int(costo)
        print("")
        print("El cambio es de: " + str(self.dinero))
        print("Muchas gracias por su compra, su articulo llegará pronto.")
