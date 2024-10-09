import os

def agregar_paciente(lista: list, numero_historia: int, nombre: str, edad: int, diagnostico: str, dias: int):
    """agrega un paciente a la lista con los datos cargados

    Args:
        lista (list): lista de pacientes
        numero_historia (int): numero de historia clinica
        nombre (str): _nombre del paciente
        edad (int): edad del paciente
        diagnostico (str): diagnostico del paciente
        dias (int): dias de internacion
    """
    lista.append([numero_historia ,nombre, edad, diagnostico, dias])

def cargar_pacientes(lista: list):
    """carga uno o mas pacientes con los datos cargados por el usuario

    Args:
        lista (list): lista de pacientes
    """
    respuesta = "si"
    while respuesta == "si":
        numero_historia = int(input("numero Historia Clinica: "))
        nombre = input("nombre: ")
        edad = int(input("edad: "))
        diagnostico = input("diagnostico: ")
        dias = int(input("dias de internacion: "))
        respuesta = input("desea cargar otro paciente: ")

        agregar_paciente(lista, numero_historia, nombre, edad, diagnostico, dias)

def mostrar_pacientes(lista: list):
    """muestra la lista de pacientes

    Args:
        lista (list): lista de pacientes
    """
    for paciente in lista:
        print(paciente)

def buscar_paciente(lista: list, numero_historia: int):
    """busca un paciente por su numero de historia clinica

    Args:
        lista (list): lista de pacientes
        numero_historia (int): numero de historia clinica a buscar

    Returns:
        _type_: retorna el paciente solicitado o un mensaje de que no lo encontro 
    """
    for paciente in lista:
        if paciente[0] == numero_historia:
            return paciente
    return f"no se encontro al paciente con el numero de historia clinica {numero_historia}"

def ordenar_lista(lista: list):
    """ordena la lista de menor a mayor por su numero de historia clinica

    Args:
        lista (list): lista de pacientes
    """

    n = len(lista)

    for i in range(n-1):       
            for j in range(n-1-i):
                if lista[j][0] > lista[j+1][0]:
                    aux = lista[j+1][0]
                    lista[j+1][0] = lista[j][0]
                    lista[j][0] = aux

def mostrar_paciente_mayor_dias_internacion(lista: list) -> int:
    """busca el paciente con mas dias de internacion

    Args:
        lista (list): lista de pacientes

    Returns:
        int: retorna el apciente con mas dias de internacion
    """
    bandera = 0
    for paciente in lista:
        if bandera == 0 or paciente[4] > paciente_mayor_dias[4]:
            paciente_mayor_dias = paciente
            bandera = 1
    return paciente_mayor_dias

def mostrar_paciente_menor_dias_internacion(lista: list) -> int:
    """busca el paciente con menos dias de internacion

    Args:
        lista (list): lista de pacientes

    Returns:
        int: retorna el apciente con menos dias de internacion
    """
    bandera = 0
    for paciente in lista:
        if bandera == 0 or paciente[4] < paciente_menor_dias[4]:
            paciente_menor_dias = paciente
            bandera = 1
    return paciente_menor_dias

def buscar_pacientes_mas_cinco_dias_internacion(lista: list) -> int:
    """da el numero de pacientes con mas de cinco dias de internacion

    Args:
        lista (list): lista de pacientes

    Returns:
        int: retorna el contador de pacientes con mas de 5 dias de internacion
    """
    contador = 0
    for paciente in lista:
        if paciente[4] >= 5:
            contador += 1
    return contador

def calcular_promedio_dias_internacion(lista: list) -> int:
    """calcula el promedio de dias de internacion de todos los pacientes

    Args:
        lista (list): lista de pacientes

    Returns:
        int: retorna el promedio de dias de internacion
    """
    promedio = 0
    for paciente in lista:
        promedio = promedio + paciente[4] 
    return promedio / len(lista)


pacientes = []
bandera_pacientes_cargados = 0

while True:
    os.system("cls")
    
    opcion = input("""
    SISTEMA DE GESTION DE CLINICA
    
    1. Cargar paciente/s 
    2. Mostrar todos los pacientes
    3. Buscar pacientes por numero de Historia Clinica
    4. Ordenar pacientes por numero de Historia Clinica
    5. Mostrar paciente con mas dias de internacion
    6. Mostrar paciente con menos dias de internacion
    7. Cantidad de pacientes con mas de 5 dias de internacion
    8. Promedio de dias de internacion de todos lo pacientes
    9. Salir
    
    elija una opcion: """)

    os.system("cls")

    match opcion:
        case "1":
            bandera_pacientes_cargados = 1
            cargar_pacientes(pacientes)
        case "2":
            if bandera_pacientes_cargados == 1:
                mostrar_pacientes(pacientes)
                input("")
            else:
                print("no hay pacientes registrados")
                input("")
        case "3":
            if bandera_pacientes_cargados == 1:
                numero_historia = int(input("ingrese el numero de historia clinica del apciente a buscar: "))
                os.system("cls")
                paciente_encontrado = buscar_paciente(pacientes, numero_historia)
                print(paciente_encontrado)
                input("")
            else:
                print("no hay pacientes registrados")
                input("")
        case "4":
            if bandera_pacientes_cargados == 1:
                ordenar_lista(pacientes)
            else:
                print("no hay pacientes registrados")
                input("")
        case "5":
            if bandera_pacientes_cargados == 1:
                paciente_mayor_dias = mostrar_paciente_mayor_dias_internacion(pacientes)
                print(f"el paciente con mayor dias de internacion es: \n{paciente_mayor_dias}")
                input("")
            else:
                print("no hay pacientes registrados")
                input("")
        case "6":
            if bandera_pacientes_cargados == 1:
                paciente_menor_dias = mostrar_paciente_menor_dias_internacion(pacientes)
                print(f"el paciente con menor dias de internacion es: \n{paciente_menor_dias}")
                input("")
            else:
                print("no hay pacientes registrados")
                input("")
        case "7":
            if bandera_pacientes_cargados == 1:
                cantidad_pacientes_mayor_cinco_dias = buscar_pacientes_mas_cinco_dias_internacion(pacientes)
                print(f"la cantidad de pacientes con mas de 5 dias de internacion es: {cantidad_pacientes_mayor_cinco_dias}")
                input("")
            else:
                print("no hay pacientes registrados")
                input("")
        case "8":
            if bandera_pacientes_cargados == 1:
                promedio = calcular_promedio_dias_internacion(pacientes)
                print(f"el promedio de dias de internacion es {promedio}")
                input("")
            else:
                print("no hay pacientes registrados")
                input("")
        case "9":
            break