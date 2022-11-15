import tkinter
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
    def __init__(self, nombre, contrasena) -> None:
        self.nombre = nombre
        self.contrasena = contrasena
        self.usuario_contrasena()

    def usuario_contrasena(self):
            usuario = input("\fIngrese su usuario: ")
            contra = input("\fIngrese su contrasena: ")
            if self.nombre == usuario and self.contrasena == contra:
                print("\fLos datos ingresados son correctos, Bienvenido a la app!")
            else:
                print("\fLos datos son incorrectos, por favor intentelo de nuevo.")
                self.usuario_contrasena()