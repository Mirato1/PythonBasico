def es_primo(numero):
    if numero == 1:
        return False
    else:
        contador = 0
    for i in range(1 , numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("Escribí un número capo: "))
    if es_primo(numero):
        print(str(numero) + " ES primo")
    else:
        print(str(numero) + " NO es primo")


if __name__ == "__main__":
    run()   
    