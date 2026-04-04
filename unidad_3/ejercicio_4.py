# Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
cerradura_forzada = 0

agente = input("ingrese el nombre del agente: ")
while not agente.isalpha():
    print("error, debe ingresar solamente letras")
    agente = input("ingrese el nombre: ")

print("ESCAPE ROOM: LA BOVEDA")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma == False:
        estado = "OFF"
    else:
        estado = "ON"
    print(f"\nCERRADURAS ABIERTAS: {cerraduras_abiertas} - ENERGIA:{energia} - TIEMPO:{tiempo} - alarma: {estado}") 
    print("\n------ MENU ------")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("seleccione una opción (1/3): ")
    
    if not opcion.isdigit():
        print("error, debe ingresar solo numeros")
        continue
    if opcion not in ["1", "2", "3"]:
        print("Opción inválida, ingrese 1, 2 o 3")
        continue

    match opcion:
        case "1":
            energia -= 20
            tiempo -= 2
            cerradura_forzada += 1
            
            if cerradura_forzada == 3:
                print("La trabó la cerradura")
                print("SE ACTIVO LA ALARMA")
                alarma = True
            
            else: 
                if energia < 40:
                    print("Hay riesgo de alarma")
                
                    numero_valido = input("selecciones un numero (1-3): ")
                    while not numero_valido.isdigit():
                        print("error, debe ingresar solamente numeros (1 o 3)")
                        numero_valido = input("selecciones un numero (1-3): ")
                    
                    if numero_valido == "3":
                        alarma = True
                        print("se prendio la alarma")

                if not alarma:
                    cerraduras_abiertas += 1
                    print("cerradura forzada correctamente")
            
        case "2":
            if energia >= 10 and tiempo >= 3:
                energia -= 10
                tiempo -= 3
                cerradura_forzada = 0
            for i in range (4):
                codigo_parcial += "E"
                print(f"paso {i + 1}: {codigo_parcial}")

                if len(codigo_parcial) >= 8:
                    cerraduras_abiertas += 1
                    print("cerradura abierta correctamente")
                    print(f"{codigo_parcial}")
                    codigo_parcial = ""

        case "3":
            print("¡DESCANSANDO...!")
            cerradura_forzada = 0
            tiempo -= 1
            if alarma:
                energia += 15 - 10
            else:
                energia += 15

            if energia > 100:
                energia = 100
            print("Descansaste, recuperaste energía")
            
        case _:
            break

print("\n------ RESULTADO ------")
if cerraduras_abiertas == 3:
    print("¡VICTORIA")

elif energia <= 0 or tiempo <= 0:
    print("DERROTA")

elif alarma == True and tiempo <= 3:
    print("DERROTA (se bloque el sistema por la alarma) ")


