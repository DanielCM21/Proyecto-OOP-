from proyecto import *
from tkinter import *


productos_express = {"1": ["Dedito", 2900], "2": ["Perro caliente", 4500], "3": ["Salchipapa", 10000], "4": ["Mazorca desgranada", 11500]}
productos_terrasse = {"1": ["Galleta", 3900], "2": ["Brownie", 3500], "3": ["Sandwich", 12500], "4": ["Cookie Pie", 18500]}
productos_cafe = {"1": ["Pasta Alfredo de Pollo", 16500], "2": ["Brownie", 3500], "3": ["Paleta", 7900], "4": ["Colombinas de Pollo", 16900]}
productos_store = {"1": ["Papita de limon", 6300], "2": ["Choclito", 7700], "3": ["Takis fuego", 3000], "4": ["Detodito picante", 7000], "5": ["Gomitas Oro", 2900], "6": ["Chicharones BBQ/Limon/Naturales", 4500], "7": ["Chocolates jumbo", 3000], "8": ["Brownie", 3500]}
alquiler_producto = {"1": ["Computador", 2000], "2": ["Guitarra", 1500], "3": ["Marcadores", 500], "4": ["Calculadora", 1000], "5":["Raqueta de tenis", 1200]}

#edificios = {"A": ["Bloque a", 3000],"B" :["Bloque b", 2500], "C" :["Bloque c", 2000], "D": ["Bloque d", 3000],"E" :["Bloque e", 2500], "F" :["Bloque f", 2000], "G" :["Bloque g", 2500], "I" :["Bloque i", 2000], "K" :["Bloque k", 2500], "J" :["Bloque J", 4000] }

GUI_Usuario()

print("\fEn Domicilios Uninorte puedes: \f\f"
            "1. Compra en establecimientos DuNord\f"
            "2. Alquiler de articulos\f")
alquier_o_compra = input("Digite que desea hacer: ")
if alquier_o_compra == "1":
        print("\fAlgunos de nuestros establecimientos disponibles son:\f\f"
                "1. DuNord Express \f"
                "2. DuNord Terrasse \f"
                "3. DuNord Cafe \f"
                "4. DuNord Store \f")

        establecimiento = input("Digite en que establecimiento desea pedir: ")
        print("")

        if establecimiento == "1":
            print("El menú disponible en el express es: \f")
            express = Pedidos_compra(productos_express)
            express.seleccionar_producto()
        elif establecimiento == "2":
            print("El menú disponible en el terrasse es: \f")
            terrasse = Pedidos_compra(productos_terrasse)
            terrasse.seleccionar_producto()
        elif establecimiento == "3":
            print("El menú disponible en el cafe es: \f")
            cafe = Pedidos_compra(productos_cafe)
            cafe.seleccionar_producto()
        elif establecimiento == "4":
            print("El menú disponible en el store es: \f")
            store = Pedidos_compra(productos_store)
            store.seleccionar_producto()
elif alquier_o_compra == "2":
        print("Los articulos disponibles para alquilar son: \f")
        alquilar = Pedidos_alquiler(alquiler_producto)
        alquilar.alquiler_articulo()








