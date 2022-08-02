
lista_numeros = [1,5, 1010, 1012]

def obtenemos2022(lista_numeros):
    lista_nueva = []
    for elemento in lista_numeros:
        lista_nueva.append(elemento)
        for segundoElemento in lista_nueva:
            print(segundoElemento)
            suma = elemento + segundoElemento

            if suma == 2022:
                print(f"El producto de los dos números es: ", elemento * segundoElemento)
                break
            else:
                print("No hay ningun numero que sume 2022")


print (obtenemos2022(lista_numeros))
