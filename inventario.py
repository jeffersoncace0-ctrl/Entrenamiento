#PEDIR NOMBRE DEL USUARIO 
nombre = input("Ingrese el nombre del producto: ")

#PEDIR PRECIO
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Valor inválido. Debe ingresar un número para el precio.")

#PEDIR CANTIDAD
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Valor inválido. Debe ingresar un número entero para la cantidad.")

#MOSTRAR LOS DATOS
print("\nDatos del producto:")
print("Nombre:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)


