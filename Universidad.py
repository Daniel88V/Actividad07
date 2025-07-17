estudiantes = {}
def ingresos():
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
        nombre = input("Ingrese el nombre del estudiante: ")
        while True:
            edad = int(input("Ingrese el edad del estudiante: "))
            if edad > 0:
                break
            else:
                print("Error, ingrese una edad valida")
        carrera = input("Ingrese la carrera del estudiante: ")
    print("¿Cuántos cursos recibirá el estudiante? ")
    cant = int(input())
    for i in range(cant):
        print(f"Curso#{i+1}")
        while True:
            clave = input("Ingrese la clave del curso: ")
            if clave in estudiantes:
                print("Error, este curso ya se ingresó")
            else:
                break
            curso = input("Ingrese el nombre del curso: ")
            nota_tarea = input("Ingrese la nota de las tareas: ")
            nota_parcial = input("Ingrese la nota del parcial: ")
            nota_proyecto = input("Ingrese la nota del proyecto: ")
        estudiantes[clave] = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera

        }