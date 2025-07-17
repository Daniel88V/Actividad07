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
            nota_tarea = int(input("Ingrese la nota de las tareas: "))
            nota_parcial = int(input("Ingrese la nota del parcial: "))
            nota_proyecto = int(input("Ingrese la nota del proyecto: "))
        estudiantes[carnet] = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera,
                "curso": {
                "codigo":clave,
                "Nota:Tarea":nota_tarea,
                "Nota:Parcial":nota_parcial,
                "Nota:Proyecto":nota_proyecto
            }
        }
def listado():
    print("---Listado de estudiantes---")
    for carnet, datos in estudiantes.items():
        print(f"Carnet: {carnet}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Edad: {datos['edad']}")
        print(f"Carrera: {datos['carrera']}")
        print(f"Curso: {datos['curso']['codigo']}")
        print(f"Curso: {datos['curso']['Nota:Tarea']}")
        print(f"Curso: {datos['curso']['Nota:Parcial']}")
        print(f"Curso: {datos['curso']['Nota:Proyecto']}")
def main():
    print("Bienvenido a la universidad")
    while True:
        print("=====MENÚ PRINCIPAL=====")
        print("1. Registrar estudiantes")
        print("2. Mostrar estudiantes y sus cursos")
        print("3. Buscar estudiante por carnet")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            ingresos()
if __name__ == "__main__":
    main()