# Diccionario principal para almacenar estudiantes
estudiantes = {}

# Función para registrar estudiantes
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    if not nombre:
        print("puede este  nombre no archivo vacío.")
        return
    if nombre in estudiantes:
        print("El estudiante ya está registrado.")
    else:
        estudiantes[nombre] = {"materias": {}}
        print(f"Estudiante {nombre} registrado exitosamente.")

def registrar_materia_nota():
    if not estudiantes:
        print("No hay estudiantes registrados. Primero registre un estudiante.")
        return
    print("Estudiantes registrados:")
    for nombre in estudiantes:
        print(f" - {nombre}")
    
    nombre = input("Ingrese el nombre del estudiante para agregar materias: ").strip()
    if nombre not in estudiantes:
        print("El estudiante no está registrado.")
        return
    agregar_mas = True
    while agregar_mas:
        materia = input("Ingrese el nombre de la materia (o 'fin' para terminar): ").strip()
        if materia.lower() == "fin":
            agregar_mas = False
            continue
        
        if not materia:
            print("El nombre de la materia no puede estar vacío.")
            continue
        
        if materia in estudiantes[nombre]["materias"]:
            print("Esta materia ya fue registrada para este estudiante.")
            continue
        
        # Validar nota
        nota_valida = False
        while not nota_valida:
            
            try:
                nota = float(input(f"Ingrese la nota de {materia} (1 a 5): "))
                if 1 <= nota <= 5:
                    nota_valida = True
                    
                else:
                    print("La nota debe estar entre 1 y 5.")
            except ValueError:
                print("Ingrese un número válido.")
                
        estudiantes[nombre]["materias"][materia] = nota
        print(f"Materia {materia} con nota {nota} registrada para {nombre}.")
        
# Función para calcular promedio
def calcular_promedio(nombre):
    materias = estudiantes[nombre]["materias"]
    if materias:
        return sum(materias.values()) / len(materias)
    else:
        return 0

# Función para mostrar información de todos los estudiantes
def mostrar_informacion():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    print("\n=== Información de todos los estudiantes ===")
    for nombre, datos in estudiantes.items():  # unpack de clave y valor
        print(f"\nEstudiante: {nombre}")
        materias = datos["materias"]
        if materias:
            for materia, nota in materias.items():  # unpack clave: valor
                print(f"  {materia}: {nota}")
            print(f"  Promedio: {calcular_promedio(nombre):.2f}")
        else:
            print("  No tiene materias registradas.")

# Función para mostrar el mejor estudiante
def mejor_estudiante():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    mejor = None
    mayor_promedio = -1
    for nombre, datos in estudiantes.items():  # unpack clave, valor
        promedio = calcular_promedio(nombre)
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            mejor = nombre
    if mejor:
        print(f"\nEl mejor estudiante es {mejor} con promedio {mayor_promedio:.2f}")
    else:
        print("No hay estudiantes con notas registradas.")

# Menú principal sin while True
def menu():
    opcion = ""
    while opcion != "5":
        print("\n--- Sistema de Gestión Académica ---")
        print("1. Registrar estudiante")
        print("2. Agregar materias y notas")
        print("3. Mostrar información de todos los estudiantes")
        print("4. Mostrar mejor estudiante")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_materia_nota()
        elif opcion == "3":
            mostrar_informacion()
        elif opcion == "4":
            mejor_estudiante()
        elif opcion == "5":
            print("Saliendo del sistema...")
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()