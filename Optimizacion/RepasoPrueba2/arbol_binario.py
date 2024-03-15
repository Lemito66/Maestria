def imprimir_nodo(nodo):
    print(nodo, end=' ')  # Imprime el valor del nodo


def imprimir_nodos_recursivo(nodo):
    if isinstance(nodo, list):
        imprimir_nodo(nodo[0])  # Imprime el valor del nodo
        for hijo in nodo[1:]:
            imprimir_nodos_recursivo(hijo)


def PRINT_NODO(arbol):
    if isinstance(arbol, list):
        imprimir_nodos_recursivo(arbol)



#arbol = [4, [3, [2, [1, [0]]]], [2, [1, [0]]], [1, [0]], [0]]
arbol = [1, [2, [5], [6]], [3], [4, [7], [8]]]

PRINT_NODO(arbol)
