activities_for_party = {
    'Carrera de sacos': True,
    'Carrera de 3 piernas': True,
    'Lanzamiento de huevo': True,
    'Carrera de relevos': False,
    'Carrera de costales': False,
    'Carrera de carretillas': False,
    'Carrera de botellas': True,
    'Carrera de globos con agua': True,
    'Carrera de huevos con cuchara': True,
    'Carrera de relevos con globos de agua': True,
    'Carrera de relevos con huevos': True,
    'Carrera de relevos con pelotas': True,
    'Carrera de relevos con vasos de agua': False,
    
}

# Solo imprimir que todavia no se han hecho elistando las actividades que estan en False

for number, activity in enumerate(activities_for_party.items()):
    #print(activity[1])
    if activity[1] == False:
        print(f'{number+1}. {activity[0]}')