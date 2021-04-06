def run():
    mi_diccionario = {
        "Llave1": 1,
        "Llave2": 2,
        "Llave3": 3,
    }
    # print(mi_diccionario["Llave1"])
    # print(mi_diccionario["Llave2"])
    # print(mi_diccionario["Llave3"])
    poblacion_paises = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }
    # print(poblacion_paises["Bolivia"])

    # for pais in poblacion_paises.keys():
    #     print(pais)
    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes.")

if __name__ == "__main__":
    run()