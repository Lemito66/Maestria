# Definir una función que eleve al cuadrado un número
def cuadrado(x):
    return x ** 2

def sum(x):
    return x + 1

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicar la función cuadrado a cada elemento de la lista usando map
resultado = map(cuadrado, numeros)

# Convertir el resultado en una lista (esto es opcional, dependiendo de tus necesidades)
resultado_lista = list(resultado)

resulta_suma = map(sum, numeros)

print(resultado_lista)
print(list(resulta_suma))


def resta(x):
    return x - 1

resulta_resta = map(resta, numeros)
print(list(resulta_resta))
