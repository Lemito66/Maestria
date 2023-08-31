MESSAGES = {
    'age_prompt': 'Ingrese su edad: ',
    'name_prompt': 'Ingrese su nombre: ',
    'confirmation_prompt': '¿Desea comprar un boleto? (S/N): ',
    'not_enough_tickets': 'No hay boletos suficientes',
    'purchase_confirmation': 'Gracias por su compra {name}, disfrute el evento',
    'visit_confirmation': 'Gracias por su visita',
    'age_restriction': 'Eres menor de edad, no puedes comprar un boleto'
}

def check_ticket_availability(number_tickets):
    return number_tickets['palco'] > 0

def sales_tickets(number_tickets):
    while check_ticket_availability(number_tickets):
        age = int(input(MESSAGES['age_prompt']))
        if age >= 18:
            name = input(MESSAGES['name_prompt'])
            
            confirmation = input(MESSAGES['confirmation_prompt'])
            if confirmation.upper() == 'S':
                how_many_ticket = int(input(f'Al momento tenemos {number_tickets["palco"]} boletos disponibles. ¿Cuantos boletos desea comprar?: '))
                if how_many_ticket > number_tickets['palco']:
                    print(MESSAGES['not_enough_tickets'])
                    break
                else:
                    number_tickets['palco'] -= how_many_ticket
                    print(MESSAGES['purchase_confirmation'].format(name=name))
            else:
                print(MESSAGES['visit_confirmation'])
                break
        else:
            print(MESSAGES['age_restriction'])
            break