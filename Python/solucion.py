def imprimir_opciones(opciones):
    '''
    Imprime las opciones del menú
    '''
    for key, value in opciones.items():
        print(key, '-->', value)


def extra(opciones):
    print('Los extras para la opción seleccionada son:\n')
    imprimir_opciones(opciones)
    extra_plato = input(
        'A continuacion ingresa el nombre de la opcion del menú que quisieras adicionar:')
    while extra_plato not in opciones:
        print('Error en selección. Por favor, revisa el menú nuevamente.')
        imprimir_opciones(opciones)

        extra_plato = input(
            'A continuacion ingresa el nombre de la opcion del menú que quisieras adicionar: ')

    costo_extra = opciones[extra_plato]
    print('La opción que seleccionaste es', extra_plato,
          'y tiene un costo adicional de $', costo_extra)
    return extra_plato, costo_extra


opciones_veg = {'Menú': 'Costo($)', 'hummus': 4,
                'tofu': 5, 'ensalada': 3, 'no extra': 0}
opciones_trad = {'Menú': 'Costo($)', 'papas': 2,
                 'empanada': 4, 'ensalada': 3, 'no extra': 0}

extra(opciones_trad) # Ejecutar la función
print(extra(opciones_veg)) # Visualizar los valores que devuelve la función
