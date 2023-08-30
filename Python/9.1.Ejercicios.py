""" 1. Escribir un programa para un restaurante que tiene un menú vegetariano y un menú tradicional (no vegetariano). Debes preguntar al cliente si es vegetariano o no para, en base a su respuesta, presentarle el menú. Para el platillo que decides ofrecer, el cliente podría escoger un ingrediente adicional (de dos o tres ingredientes). Presenta también un pequeño menú de bebidas frías y calientes. """

menus = {
    'tradicional': {
        'entrada': 'Sopa',
        'fuerte': 'Carne',
        'postre': 'Helado',
    },
    'vegetariano': {
        'entrada': 'Ensalada',
        'fuerte': 'Pizza',
        'postre': 'Fruta',
    }
}

drinks = {
    'frias': ['Coca Cola', 'Fanta', 'Sprite'],
    'calientes': ['Café', 'Té', 'Chocolate'],
}



def ask_for_ingredients():
    list_of_aditional_ingredients = []
    how_many_ingredientes = int(
        input('¿Cuántos ingredientes quieres agregar? (Máximo 3): '))
    while how_many_ingredientes not in [1, 2, 3]:
        print('Ingresa un número válido')
        how_many_ingredientes = int(
            input('¿Cuántos ingredientes quieres agregar? (Máximo 3): '))

    for ingredient in range(how_many_ingredientes):
        additional_ingredient = input('Ingresa el ingrediente adicional: ')
        list_of_aditional_ingredients.append(additional_ingredient)

    return list_of_aditional_ingredients


def show_drinks_menu(type_of_drinks):

    if type_of_drinks == 1:
        for number, drink in enumerate(drinks['calientes']):
            print(f'{number+1}. {drink}')
    elif type_of_drinks == 2:
        for number, drink in enumerate(drinks['frias']):
            print(f'{number+1}. {drink}')


while True:
    question = input("""¿Qué menú quieres?
                     Escribe "tradicional" o "vegetariano"
    """).lower()

    if question in ['tradicional', 'vegetariano']:
        menu_type = menus[question]
        print(f'El menú {question} es:')
        for key, value in menu_type.items():
            print(f'{key}: {value}')

        if question == 'tradicional':
            question_ingredient = input(
                '¿Quieres agregar ingredientes adicionales? (S/N): ').lower()
            if question_ingredient == 's':
                ingredientes_adicionales = ask_for_ingredients()
                menu_type['ingredientes adicionales'] = ingredientes_adicionales

            drinks_option = int(input(
                'Tenemos bebidas calientes y frias, presiona 1 para bebidas calientes y 2 para bebidas frias: ').lower())
            while drinks_option not in [1, 2]:
                print('Ingresa un número válido')
                drinks_option = int(input(
                    'Tenemos bebidas calientes y frias, presiona 1 para bebidas calientes y 2 para bebidas frias: ').lower())
            show_drinks_menu(drinks_option)
            type_of_drink = input('Seleccione el número de la bebida: ')
            while int(type_of_drink) not in [1, 2, 3]:
                print('Ingresa un número válido')
                type_of_drink = input('Seleccione el número de la bebida: ')
            menu_type['bebida'] = drinks['calientes'][int(type_of_drink)-1]

        elif question == 'vegetariano':
            question_ingredient = input(
                '¿Quieres agregar ingredientes adicionales? (S/N): ').lower()
            if question_ingredient == 's':
                ingredientes_adicionales = ask_for_ingredients()
                menu_type['ingredientes adicionales'] = ingredientes_adicionales

            drinks_option = int(input(
                'Tenemos bebidas calientes y frias, presiona 1 para bebidas calientes y 2 para bebidas frias').lower())
            while drinks_option not in [1, 2]:
                print('Ingresa un número válido')
                drinks_option = input(
                    'Tenemos bebidas calientes y frias, presiona 1 para bebidas calientes y 2 para bebidas frias').lower()
            show_drinks_menu(drinks_option)
            type_of_drink = input('Seleccione el número de la bebida: ')
            while int(type_of_drink) not in [1, 2, 3]:
                print('Ingresa un número válido')
                type_of_drink = input('Seleccione el número de la bebida: ')
            menu_type['bebida'] = drinks['calientes'][int(type_of_drink)-1]

        break
    else:
        print('Escribe "tradicional" o "vegetariano"')

print('\nSu orden es la siguiente:')
for key, value in menu_type.items():
    if key == 'Ingredientes adicionales':
        print(f'Ingredientes adicionales: {", ".join(value)}')
    else:
        print(f'{key}: {value}')


# print([x + 1 for x in range(len(drinks['calientes']))])
