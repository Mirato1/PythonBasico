import random


# def run():
#     numero_aleatorio = random.randint(1, 100)
#     numero_usuario = int(input("Elige un número del 1 al 100: "))
#     while numero_usuario != numero_aleatorio:
#         if numero_usuario < numero_aleatorio:
#             print("Busca un número más grande")
#         else:
#             print("Busca un número más pequeño")
#         numero_usuario = int(input("Elige otro número: "))
#     print("¡Ganaste!")


# if __name__ == "__main__":
#     run()


def run():
    numerorandom = random.randint(1, 50)
    numeroelegido = int(input("Introduce un numero: "))
    vidas = 5
    while numerorandom != numeroelegido :
        if numerorandom < numeroelegido : 
            print("Elige un numero mas pequeño.")
            vidas -= 1
        elif numerorandom > numeroelegido : 
            print("Elige un numero mas grande.")
            vidas -= 1
        if vidas == 0 :
            print("GAME OVER")
            break
        print("Tienes", vidas, "vidas")
        numeroelegido = int(input("Introduce numero: "))
    if numerorandom == numeroelegido : 
        print("FELICIDADES GANASTE")


if __name__ == "__main__" : 
    run()