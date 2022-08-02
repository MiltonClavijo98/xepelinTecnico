#Parantesis balanceados

"""Entradas posibles:

A) "()" -> True
B) "(" -> False
C) ")" -> False

"""

def paratensisBalanceados(cadena):
    abiertos = 0
    parentesisAbierto = "("
    paratensisCerrado = ")"

    for caracter in cadena:
        if caracter in parentesisAbierto:
            abiertos += 1
        elif caracter in paratensisCerrado:
            abiertos -= 1

    if abiertos < 0 or abiertos > 0:
        return False
    elif caracter not in paratensisCerrado or caracter not in parentesisAbierto:
        print('El string no tiene parantesis')
    else:
        return True

print(paratensisBalanceados("Hola"))
