usuario = "alumno"
clave = "python123"

intentos = 0
intentos_maximos = 3
acceso = False

while intentos < intentos_maximos:
    intentos += 1
    usuario_ingresado = input(f"intento {intentos}/{intentos_maximos} - ingrese el usuario: ")
    clave_ingresada = input("ingrese la clave: ")

    if usuario_ingresado == usuario and clave_ingresada == clave:
        print("Acceso concedido. Bienvenido al campus de la UTN")
        acceso = True
        break
    else:
        print("Error,credenciales invalidas.")
    if intentos == intentos_maximos:
        print("Cuenta bloqueda.")

while acceso:
    print("\n------CAMPUS UTN------")
    print("1. Ver estado de inscripción")
    print("2. Cambiar clave")
    print("3. Mostrar mensaje motivacional")
    print("4. Salir")

    opcion = input("seleccione una opción (1/4): ")
    
    if not opcion.isdigit():
        print("error, debe ingresar solo numeros")
        continue
    
    match opcion:
        case "1":
            print("Estado: Inscripción Activa")
        
        case "2":
            nueva_clave = input("ingrese nueva clave: ")
            confirmacion = input("confirme la clave: ")
            if len(nueva_clave) < 6:
                print("error, minimo 6 caracteres")
            elif nueva_clave == confirmacion and len(nueva_clave) > 6:
                print("La clave se cambio exitosamente")
            else:
                print("error, la nueva clave debe coincidir con la confirmacion")
        
        case "3":
            print("¡Seguí adelante, tu esfuerzo tiene recompensa")
            
        case "4":
            print("saliendo...")
            print("Hasta Luego")
            acceso = False

        case _:
            print("Opcion invalida")

