estudiantes = {}
print("¿Cuántos estudiantes desea ingresar? ")
cantidad = int(input())
for i in range(cantidad):
    print(f"Estudiante#{i+1}")
    while True:
        carnet = input("Ingrese el carnet del estudiante: ")
        if carnet in estudiantes:
            print("Error, este estudiante ya existe")
        else:
            break
    nombre = input(f"Ingrese el nombre del estudiante: ")
    while True:
        edad = int(input("Ingrese el edad del estudiante: "))
        if edad > 0:
            break
        else:
            print("Error, ingrese una edad valida")
    carrera = input("Ingrese la carrera del estudiante: ")
    print("¿Cuántos cursos recibirá el estudiante? ")
    cant = int(input())
    for j in range(cant):
        print(f"Curso#{j+1}")
        while True:
            clave = input("Ingrese la clave del curso: ")
            if clave in estudiantes:
                print("Error, este curso ya se ingresó")
            else:
                break
        nota_tarea = int(input("Ingrese la nota de las tareas: "))
        nota_parcial = int(input("Ingrese la nota del parcial: "))
        nota_proyecto = int(input("Ingrese la nota del proyecto: "))
    estudiantes[carnet] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "curso": {
            "codigo":clave,
            "NotaTarea":nota_tarea,
            "NotaParcial":nota_parcial,
            "NotaProyecto":nota_proyecto
            }
        }
print("\t Bienvenido a la universidad")
while True:
    print("=====MENÚ PRINCIPAL=====")
    print("1. Listado de estudiantes")
    print("2. Buscar estudiante por carnet")
    print("3. Salir")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        print("\t ---Listado de estudiantes---")
        for carnet, datos in estudiantes.items():
            print(f"Carnet: {carnet}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Edad: {datos['edad']}")
            print(f"Carrera: {datos['carrera']}")
            print(f"Curso: {datos['curso']['codigo']}")
            print(f"Nota de las tareas: {datos['curso']['NotaTarea']}")
            print(f"Nota del parcial: {datos['curso']['NotaParcial']}")
            print(f"Nota del proyecto: {datos['curso']['NotaProyecto']}")
    elif opcion == "2":
        print("\t Ingrese el carnet del estudiante que desea ver: ")
        alumno = input()
        if alumno in estudiantes:
            print(f"Nombre: {estudiantes[alumno]['nombre']}")
            print(f"Edad: {estudiantes[alumno]['edad']}")
            print(f"Carrera: {estudiantes[alumno]['carrera']}")
            print(f"Curso: {estudiantes[alumno]['curso']['codigo']}")
            print(f"Nota de las tareas: {estudiantes[alumno]['curso']['NotaTarea']}")
            print(f"Nota del parcial: {estudiantes[alumno]['curso']['NotaParcial']}")
            print(f"Nota del proyecto: {estudiantes[alumno]['curso']['NotaProyecto']}")
        else:
            print("No existe un estudiante con este carnet")
    elif opcion == "3":
        exit()