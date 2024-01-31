# multiplicacion de matricees 4*4 con python 

import numpy as np 

p_ = [[0.8, 0.2], [0.6, 0.4]]

# multiplicar matrices

p_2 = np.dot(p_, p_)

print(p_2)

p_3 = np.dot(p_2, p_)

print(p_3)

p_4 = np.dot(p_3, p_)

print(p_4) 

# ejercicio dos

multiplicacion = np.dot([0.9,0.1], [[0.85, 0.15], [0.4, 0.6]])



#print(multiplicacion_2)

#multiplicacion_3 = np.dot(multiplicacion_2, [[0.85, 0.15], [0.4, 0.6]])

#print(multiplicacion_3)

# matriz de transicion al año 2

multiplicacion2 = np.dot([[0.85, 0.15], [0.4, 0.6]], [[0.85, 0.15], [0.4, 0.6]])
print(multiplicacion2)

multiplicacion3 = np.dot([0.9, 0.1], multiplicacion2)
print(multiplicacion3)

# esta matriz multiplicado para 25 años

p_25 = [[0.85, 0.15], [0.4, 0.6]]

for i in range(26):
    p_25 = np.dot(p_25, [[0.85, 0.15], [0.4, 0.6]])
print(p_25)


p_20 = [0.9, 0.1]

for i in range(21):
    p_20 = np.dot(p_20, [[0.72, 0.28], [0.72, 0.28]])
    
print(p_20)
