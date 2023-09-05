
lista_de_cosas_fiesta = {
    'beber': True,
    'comer': True,
    'bailar': True,
    'cantar': True,
    'jugar': True,
    'dormir': False,
    'reir': True,
    'llorar': False,
    'trabajar': False,
    'estudiar': False,
    'programar': False,
    'cocinar': True,
}

for key, value in lista_de_cosas_fiesta.items():
    if value == False:
        print(key)

# La gasolina de un carro se acaba en 1000 km.

kilometros_recorridos = 995

while kilometros_recorridos <= 1000:
    print(f'Tienes {kilometros_recorridos} te faltan {1000 - kilometros_recorridos} para llegar a tu destino')
    kilometros_recorridos +=1