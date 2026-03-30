# Lista global
estudiantes = []

# =========================
# VALIDACIONES
# =========================
def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_edad(edad):
    return edad.isdigit() and 0 < int(edad) < 120

def validar_id(id_estudiante):
    return id_estudiante.isdigit()


# =========================
# FUNCIONES
# =========================
def registrar_estudiante():
    print("\n--- Registrar Estudiante ---")
    
    id_estudiante = input("ID: ")
    if not validar_id(id_estudiante):
        print("Error: El ID debe ser numérico")
        return

    # Validar ID duplicado
    for e in estudiantes:
        if e["id"] == id_estudiante:
            print("Error: El ID ya existe")
            return

    nombre = input("Nombre: ")
    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío")
        return

    edad = input("Edad: ")
    if not validar_edad(edad):
        print("Error: Edad inválida")
        return

    curso = input("Curso: ")
    estado = input("Estado (activo/inactivo): ")

    estudiante = {
        "id": id_estudiante,
        "nombre": nombre,
        "edad": int(edad),
        "curso": curso,
        "estado": estado
    }

    estudiantes.append(estudiante)
    print("Estudiante registrado correctamente")


def ver_estudiantes():
    print("\n--- Lista de Estudiantes ---")

    if not estudiantes:
        print("No hay estudiantes registrados")
        return

    for e in estudiantes:
        print(f'ID: {e["id"]} | Nombre: {e["nombre"]} | Edad: {e["edad"]} | Curso: {e["curso"]} | Estado: {e["estado"]}')


def buscar_estudiante():
    print("\n--- Buscar Estudiante ---")

    busqueda = input("Ingrese ID o Nombre: ")
    encontrado = False

    for e in estudiantes:
        if e["id"] == busqueda or e["nombre"].lower() == busqueda.lower():
            print(f'Encontrado -> ID: {e["id"]} | Nombre: {e["nombre"]}')
            encontrado = True

    if not encontrado:
        print("Estudiante no encontrado")


def actualizar_estudiante():
    print("\n--- Actualizar Estudiante ---")

    id_estudiante = input("Ingrese el ID: ")

    for e in estudiantes:
        if e["id"] == id_estudiante:

            nuevo_nombre = input("Nuevo nombre: ")
            if validar_nombre(nuevo_nombre):
                e["nombre"] = nuevo_nombre

            nueva_edad = input("Nueva edad: ")
            if validar_edad(nueva_edad):
                e["edad"] = int(nueva_edad)

            e["curso"] = input("Nuevo curso: ")
            e["estado"] = input("Nuevo estado: ")

            print("Estudiante actualizado correctamente")
            return

    print("Estudiante no encontrado")


def eliminar_estudiante():
    print("\n--- Eliminar Estudiante ---")

    id_estudiante = input("Ingrese el ID: ")

    for e in estudiantes:
        if e["id"] == id_estudiante:
            estudiantes.remove(e)
            print("Estudiante eliminado")
            return

    print("Estudiante no encontrado")


# =========================
# MENÚ
# =========================
def menu():
    opcion = ""

    while opcion != "6":
        print("\n===== MENÚ =====")
        print("1. Registrar estudiante")
        print("2. Ver estudiantes")
        print("3. Buscar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            ver_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            actualizar_estudiante()
        elif opcion == "5":
            eliminar_estudiante()
        elif opcion == "6":
            print("Hasta luego")
        else:
            print("Opción inválida")


# Ejecutar programa
menu()
