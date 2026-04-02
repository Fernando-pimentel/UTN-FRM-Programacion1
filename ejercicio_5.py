# Ejercicio 5

vida_gladiador = 100 
vida_enemigo = 100 
pociones_de_vida = 3 
daño_base = 15 
daño_base_enemigo = 12 
turno_gladiador = True 

print("---- BIENVENIDOS A LA ARENA ----")
nombre_gladiador = input("Nombre del gradiador: ")

while not nombre_gladiador.isalpha():
    print("error, debe ingresar solamente letras")
    nombre_gladiador = input("Nombre del gradiador: ")

print("=== INICIO DEL COMBATE ===")
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"\n{nombre_gladiador} HP:{vida_gladiador} vs Enemigo HP: {vida_enemigo} - pociones: {pociones_de_vida}")
    if turno_gladiador:
        print("\n------ Elige una opción ------")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")
        opcion = input("Opción: ")
    
        if not opcion.isdigit():
            print("error, debe ingresar solo numeros")
            opcion = input("Opción: ")
        match opcion:
            case "1":
                print("¡Inicias con un Ataque Pesado!")
                daño = daño_base
                if vida_enemigo > 20:
                    vida_enemigo -= 15
                    print(f"Atacaste al enemigo por {daño} puntos de daños")
                    turno_gladiador = False
                elif vida_enemigo < 20:
                    daño *= 1.5
                    daño = int(daño)
                    vida_enemigo -= daño
                    print(f"Atacaste al enemigo por {daño} puntos de daños")
                    turno_gladiador = False
                    
            case "2":
                print("¡Inicias con una Rafada de golpes!")
                for i in range(3):
                    vida_enemigo -= 5
                    print("Golpe conectado por 5 de daño")
                    turno_gladiador = False
            case "3":
                if pociones_de_vida > 0:
                    vida_gladiador += 30
                    pociones_de_vida -= 1

                else:
                    print("¡No quedan pociones!")
                    turno_gladiador = False
                
            case _:
                print("Error, opcion invalida")
                continue
    
    else:
        vida_gladiador -= daño_base_enemigo
        print(f"El enemigo contraataca e hizo {daño_base_enemigo} de daño")
        turno_gladiador = True

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla")

else:
    print("Perdiste...")

    
            
