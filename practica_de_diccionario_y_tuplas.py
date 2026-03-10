

vuelos = {"AV101": ("Bogota", 5 , 300),
    "AV202": ("Medellin", 3 , 200),
    "AV303": ("Cartagena", 2, 220),
    "AV404": ("Cali", 4, 250)}

reservas =[]

print ("Bienvenido al sistema de reservas de vuelos")

opcion = "si"

while opcion.lower () == "si":
    nombre = input("Ingrese el nombre del pasajero: ")
    codigo = input("Ingrese el código del vuelo: ")
    
    if codigo in vuelos:
        destino,asientos_disponible,  precio = vuelos[codigo]
        cantidad_de_asientos = int(input ("Ingrese la cantidad de asientos a reservar: "))
        
        if cantidad_de_asientos <= asientos_disponible: 
            reservas.append((nombre, codigo, cantidad_de_asientos))
            
            vuelos[codigo] = (destino, asientos_disponible - cantidad_de_asientos, precio) 
            print(f"Reserva confirmada para {nombre} en el vuelo {codigo} hacia {destino}.")
            print(f"Asientos restantes en el vuelo {codigo}: {vuelos[codigo][1]}")
    else:
        print ("Código de vuelo no válido. Por favor, intente nuevamente.") 
        
    opcion = input("¿Desea hacer otra reserva? (si/no): ")  
    
    print("\nReservas realizadas:")
    for reserva in reservas:
        print(f"Pasajero: {reserva[0]}, Código de vuelo: {reserva[1]}, Asientos reservados: {reserva[2]}") 
