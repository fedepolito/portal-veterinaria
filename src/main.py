import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

REGISTRADOS_PATH = os.path.join(DATA_DIR, "registrados.txt")
ELIMINADOS_PATH = os.path.join(DATA_DIR, "eliminados.txt")

ARCHIVO_REGISTRADOS = "registrados.txt"
ARCHIVO_ELIMINADOS = "eliminados.txt"


def mostrar_menu():
    print("\n--- Veterinaria 'Tu mascota feliz' ---")
    print("1. Registrar paciente")
    print("2. Consultar registros")
    print("3. Modificar registro")
    print("4. Eliminar registro")
    print("5. Salir")


def pedir_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        if 1 <= opcion <= 5:
            return opcion
        else:
            print("Opción inválida. Elegí entre 1 y 5.")
    except ValueError:
        print("Debés ingresar un número.")
    return None


def cargar_pacientes():
    pacientes = []
    try:
        with open(REGISTRADOS_PATH, "r") as archivo:
            for linea in archivo:
                pacientes.append(linea.strip().split("|"))
    except FileNotFoundError:
        open(REGISTRADOS_PATH, "w").close()
    return pacientes


def guardar_pacientes(pacientes):
    with open(REGISTRADOS_PATH, "w") as archivo:
        for p in pacientes:
            archivo.write("|".join(map(str, p)) + "\n")


def agregar_paciente(pacientes):
    nombre = input("Nombre: ")

    while True:
        sexo = input("Sexo (M/F/Masculino/Femenino): ").capitalize()
        if sexo in ("M", "F", "Masculino", "Femenino"):
            break
        print("Sexo inválido.")

    try:
        edad = int(input("Edad aproximada: "))
    except ValueError:
        print("Edad inválida.")
        return

    while True:
        especie = input("Especie (Canino/Felino): ").capitalize()
        if especie in ("Canino", "Felino"):
            break
        print("Especie inválida.")

    rasgos = input("Rasgos: ")
    enfermedad = input("Enfermedad: ")
    duenio = input("Nombre del dueño: ")
    telefono = input("Número de contacto: ")

    pacientes.append([nombre, sexo, edad, especie, rasgos, enfermedad, duenio, telefono])
    guardar_pacientes(pacientes)
    print("Paciente registrado correctamente.")


def mostrar_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    for i, p in enumerate(pacientes, start=1):
        print(f"\nID {i}")
        print(f"Nombre       : {p[0]}")
        print(f"Sexo         : {p[1]}")
        print(f"Edad         : {p[2]}")
        print(f"Especie      : {p[3]}")
        print(f"Rasgos       : {p[4]}")
        print(f"Enfermedad   : {p[5]}")
        print(f"Dueño        : {p[6]}")
        print(f"Teléfono     : {p[7]}")


def modificar_paciente(pacientes):
    mostrar_pacientes(pacientes)
    if not pacientes:
        return

    try:
        indice = int(input("ID del paciente a modificar: ")) - 1
        if indice < 0 or indice >= len(pacientes):
            print("ID inválido.")
            return
    except ValueError:
        print("ID inválido.")
        return

    campos = [
        "Nombre", "Sexo", "Edad", "Especie",
        "Rasgos", "Enfermedad", "Dueño", "Teléfono"
    ]

    for i, campo in enumerate(campos, start=1):
        print(f"{i}. {campo}")

    try:
        campo_id = int(input("Campo a modificar: ")) - 1
        if campo_id < 0 or campo_id >= len(campos):
            print("Campo inválido.")
            return
    except ValueError:
        print("Campo inválido.")
        return

    nuevo_valor = input("Nuevo valor: ")
    pacientes[indice][campo_id] = nuevo_valor
    guardar_pacientes(pacientes)
    print("Registro actualizado correctamente.")


def eliminar_paciente(pacientes):
    mostrar_pacientes(pacientes)
    if not pacientes:
        return

    try:
        indice = int(input("ID del paciente a eliminar: ")) - 1
        if indice < 0 or indice >= len(pacientes):
            print("ID inválido.")
            return
    except ValueError:
        print("ID inválido.")
        return

    eliminado = pacientes.pop(indice)

    with open(ELIMINADOS_PATH, "a") as archivo:
        archivo.write("|".join(map(str, eliminado)) + "\n")

    guardar_pacientes(pacientes)
    print("Paciente eliminado correctamente.")


def main():
    pacientes = cargar_pacientes()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            agregar_paciente(pacientes)
        elif opcion == 2:
            mostrar_pacientes(pacientes)
        elif opcion == 3:
            modificar_paciente(pacientes)
        elif opcion == 4:
            eliminar_paciente(pacientes)
        elif opcion == 5:
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    main()