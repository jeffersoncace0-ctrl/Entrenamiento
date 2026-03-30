
filas = 8
columnas = 10


sala = [["_"] * columnas for _ in range(filas)]

def mostrar_sala():
    print("\nSALA DE CINE")
    for fila in sala:
        print(" ".join(fila))
        
def ocupar_asiento(fila, columna):
    if 0 <= fila < filas and 0 <= columna < columnas:
        if sala[fila][columna] == "_":
            sala[fila][columna] = 'X'
            print("Asiento reservado.")
        else:
            print("El asiento ya está ocupado.")
    else:
        print("Fila o columna fuera de rango.")

while True:
    mostrar_sala()
    fila = int(input("Elige la fila (1-8): ")) - 1
    columna = int(input("Elige la columna (1-10): ")) - 1
    ocupar_asiento(fila, columna)
    otra = input("¿Reservar otro asiento? (si/no): ")
    if otra.lower() != "si":
        break

print("\nEstado final de la sala:")
mostrar_sala() 