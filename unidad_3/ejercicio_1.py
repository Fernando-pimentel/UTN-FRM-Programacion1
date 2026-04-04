# EJERCICIO 1 

cliente = input("ingrese el nombre del cliente: " )

while not cliente.isalpha():
    print("error, debe ingresar solamente letras")
    cliente = input("ingrese el nombre del cliente: ")

cantidad = input("ingrese la cantidad de productos que desea comprar: ")
total_sin_descuento = 0
total_con_descuento = 0

while not cantidad.isdigit() or int(cantidad) == 0:
    print("error, ingrese un numero entero positivo")
    cantidad = input("ingrese la cantidad de productos que desea comprar: ")

cantidad = int(cantidad)

for i in range(1, cantidad + 1):
    print(f"producto {i}")

    precio = input("ingrese el precio del producto: ")
    
    while not precio.isdigit():
        print("error, ingrese solo numeros enteros")
        precio = input("ingrese la cantidad de productos que desea comprar: ")
    precio = float(precio)

    descuento = input("¿el producto tiene descuento? (s/n): ").lower()
    while descuento != "s" and descuento != "n":
        print("por favor, ingrese (s/n)")
        descuento = input("¿el producto tiene descuento? (s/n): ").lower()
    
    total_sin_descuento += precio

    if descuento == "s":
        precio_final = precio - (precio * 0.10)
    
    else:
        precio_final = precio 
    
    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio_por_producto = total_sin_descuento / cantidad

print("")
print("-------- TICKET DE COMPRA --------")
print(f"cliente: {cliente}")
print(f"cantidad de producto: {cantidad}")
print(f"total sin descuentos: {total_sin_descuento}")
print(f"total con descuentos: {total_con_descuento}")
print(f"ahorro: {ahorro}")
print(f"promedio por producto: {promedio_por_producto:.2f}")

