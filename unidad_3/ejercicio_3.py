# ejercicio 3 
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

nombre = input("ingrese el nombre: ")
while not nombre.isalpha():
    print("error, debe ingresar solamente letras")
    nombre = input("ingrese el nombre: ")
    

opcion = 0
while opcion != "5":
    print("\n" + "=" * 50)
    print("---------- Agenda de turnos ----------")
    print("=" * 50)
    print("1. RESERVAR TURNO")
    print("2. CANCELAR TURNO (POR NOMBRE)")
    print("3. VER AGENDA DEL DIA")
    print("4. VER RESUMEN GENERAL")
    print("5. CERRAR SISTEMA")

    opcion = input("seleccione una opción (1/5): ")

    match opcion:
        case "1":
            dia = input("ingrese el dia a reservar (1=lunes/2=martes): ")
            while dia != "1" and dia != "2":
                print("error, ingrese (1/2)")
                dia = input("ingrese el dia a reservar (1=lunes/2=marte): ")
            
            if dia == "1":
                if lunes1 != "" and lunes2 != "" and lunes3 != "" and lunes4 != "":
                    print("No hay turnos disponibles")
                else: 
                    paciente = input("ingrese el nombre del paciente: ")
                    while not paciente.isalpha():
                        print("error, debe ingresar solamente letras")
                        paciente = input("ingrese el nombre del paciente: ")
                    
                    if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                        print("ese nombre ya tiene reservado el dia lunes")
                    else:                                
                        if lunes1 == "":
                            lunes1 = paciente
                        elif lunes2 == "":
                            lunes2 = paciente
                        elif lunes3 == "":
                            lunes3 = paciente
                        elif lunes4 == "":
                            lunes4 = paciente
                        else:
                            print("No hay turnos disponibles")
            if dia == "2":
                if martes1 != "" and martes2 != "" and martes3 != "":
                    print("No hay turnos disponibles")
                else: 
                    paciente = input("ingrese el nombre del paciente: ")
                    while not paciente.isalpha():
                        print("error, debe ingresar solamente letras")
                        paciente = input("ingrese el nombre del paciente: ")
                    if paciente == martes1 or paciente == martes2 or paciente == martes3:
                        print("ese nombre ya tiene reservado el dia martes")
                    else:    
                        if martes1 == "":
                            martes1 = paciente
                        elif martes2 == "":
                            martes2 = paciente
                        elif martes3 == "":
                            martes3 = paciente
                        else:
                            print("No hay turnos disponibles")
                
        case "2":
            dia = input("ingrese el dia (1=lunes/2=martes): ")
            while dia != "1" and dia != "2":
                print("error, ingrese (1/2)")
                dia = input("ingrese el dia a reservar (1=lunes/2=marte): ")
            while True:
                paciente = input("ingrese el nombre del cliente a cancelar: ")
                if paciente.isalpha():
                    break
                else:
                    print("error, debe ingresar solo letras: ")

            if dia == "1":
                if lunes1 == paciente:
                    lunes1 = ""
                    print("El turno fue cancelado")
                elif lunes2 == paciente:
                    lunes2 = ""
                    print("El turno fue cancelado")
                elif lunes3 == paciente:
                    lunes3 = "" 
                    print("El turno fue cancelado")
                elif lunes4 == paciente:
                    lunes4 = ""
                    print("El turno fue cancelado")
                else:
                    print(f"{paciente} no tiene turno reservado el dia lunes")

            if dia == "2":
                if martes1 == paciente:
                    martes1 = ""
                    print("El turno fue cancelado")                    
                elif martes2 == paciente:
                    martes2 = ""
                    print("El turno fue cancelado")
                elif martes3 == paciente:
                    martes3 = "" 
                    print("el turno fue cancelado")
                else:
                    print(f"{paciente} no tiene turno reservado el dia martes")

        case "3":
            dia = input("ingrese el dia (1=lunes/2=martes): ")
            while dia != "1" and dia != "2":
                print("error, ingrese (1/2)")
                dia = input("ingrese el dia a reservar (1=lunes/2=marte): ")

            if dia == "1":
                print("\n Agenda Lunes")
                if lunes1 == "":
                    print("Turno 1: libre")
                else:
                    print("Turno 1:", lunes1)
                if lunes2 == "":
                    print("Turno 2: libre")
                else:
                    print("Turno 2:", lunes2)
                if lunes3 == "":
                    print("Turno 3: libre")
                else:
                    print("Turno 3:", lunes3)
                if lunes4 == "":
                    print("Turno 4: libre")
                else:
                    print("Turno 4:", lunes4)

            if dia == "2":
                print("\n Agenda Martes")
                if martes1 == "":
                    print("Turno 1: libre")
                else:
                    print("Turno 1:", martes1)
                if martes2 == "":
                    print("Turno 2: libre")
                else:
                    print("Turno 2:", martes2)
                if martes3 == "":
                    print("Turno 3: libre")
                else:
                    print("Turno 3:", martes3)

        case "4":
            ocupados_lunes = 0
            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1

            libres_lunes = 4 - ocupados_lunes
            
            ocupados_martes = 0
            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1
            
            libres_martes = 3 - ocupados_martes

            print("\n--------Resumen General--------")
            print("\nLunes:")
            print("ocupados:", ocupados_lunes)
            print("disponibles:", libres_lunes)

            print("\nmartes:")
            print("ocupados:", ocupados_martes)
            print("disponibles:", libres_martes)
            
            if ocupados_lunes > ocupados_martes:
                print("El dia con mas turnos fue el Lunes")
            if ocupados_lunes < ocupados_martes:
                print("El dia con mas turnos fue el Martes")

        case "5":
            print("\n---Cerrando el sistema---")
            print("Hasta luego")
               
