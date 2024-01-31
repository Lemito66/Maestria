# Juego ruleta

import numpy as np

probabilidades = [
    [1, 0, 0, 0, ],
    [0.5, 0, 0.5, 0, ],
    [0, 0.5, 0, 0.5, ],
    [0, 0, 0, 1, ],
]

#multiplicacion = np.dot(probabilidades, probabilidades)
multiplicacion = probabilidades
for i in range(10):
    multiplicacion = np.dot(multiplicacion, probabilidades)
print(multiplicacion)

estado_inicial = [0, 0, 1, 0]

multiplicacion_2 = np.dot(estado_inicial, multiplicacion)

print(multiplicacion_2)



