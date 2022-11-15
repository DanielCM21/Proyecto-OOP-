from tkinter import *

class GUI_Usuario:
    
    def __init__(self) -> None:
        self.ventanaDeCompra = ventanadecompra()
        self.raiz=Tk()
        self.raiz.resizable(False, False)
        self.raiz.title("Domicilios Uninorte")
        self.raiz.iconbitmap("domicilios_uninorte.ico")
        self.frame1= Frame(self.raiz, width=300, height=500)
        self.frame1.pack()

        self.cuadroUsuario=Entry(self.frame1)
        self.cuadroUsuario.grid(row=1, column=1, padx=10, pady=10)
        usuarioLabel=Label(self.frame1, text="Usuario: ")
        usuarioLabel.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.cuadroContrasena=Entry(self.frame1)
        self.cuadroContrasena.grid(row=2, column=1, padx=10, pady=10)
        self.cuadroContrasena.config(show="*")
        contrasenaLabel=Label(self.frame1, text="Contraseña: ")
        contrasenaLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        botonConfirmar= Button(self.frame1, text="Confirmar")
        botonConfirmar.grid(row=3, column=1, padx=10, pady=10)

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

class Usuarios:
    def __init__(self, cuadroUsuario, cuadroContrasena) -> None:
        self.nombre = cuadroUsuario
        self.contrasena = cuadroContrasena
        self.usuario_contrasena()

    def usuario_contrasena(self):
            usuario = input("\fIngrese su usuario: ")
            contra = input("\fIngrese su contrasena: ")
            if self.nombre == usuario and self.contrasena == contra:
                print("\fLos datos ingresados son correctos, Bienvenido a la app!")
            else:
                print("\fLos datos son incorrectos, por favor intentelo de nuevo.")
                self.usuario_contrasena()

class ventanadecompra:
    def __init__(self) -> None:
        pass
    def crearventana(self):
        self.raiz=Tk()
        self.raiz.resizable(False, False)
        self.raiz.title("Domicilios Uninorte")
        self.raiz.iconbitmap("domicilios_uninorte.ico")
