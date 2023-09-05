#La cadena ingresada es palíndrome o no
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

''' print(is_palindrome("anita lava la tina"))
print(is_palindrome("ana"))
print(is_palindrome("ana ana"))
print(is_palindrome("ana ana ana"))
print(is_palindrome("Emill Logroño")) '''

'''
1. Hacer que el usuario ingrese 5 palabras por consola e indicarle, por cada palabra ingresada, si la letra de inicio es igual a la letra final (use una función que retorne True o False de ser el caso).
'''

def verify_word(word):
    return word[0] == word[-1]

'''for i in range(5):
    word = input("Ingrese una palabra: ")
    print(verify_word(word.lower())) '''


'''
4. Calcular la suma y el promedio de los dígitos que estén presentes en una cadena de texto
'''

def only_numbers(string):
    return [int(character) for character in string if character.isdigit()]
    '''numbers = []
    for character in string:
        if character.isdigit():
            numbers.append(int(character))
    return numbers '''


def sum_and_average(string):
    numbers = only_numbers(string)
    return sum(numbers), sum(numbers) / len(numbers)

#print(sum_and_average("ho5la 1234"))


''' 3. Has implementado tu diccionario Palabritas.com donde el usuario ingresa una palabra y tú le presentas la definición. Considera: (1) que independientemente de si el usuario ingresa mayúsculas, la búsqueda sea en minúsculas; (2) que el usuario ingrese sólo una palabra para poder hacer la búsqueda; (3) que independientemente de si el usuario ingresa espacios en blanco al inicio o al final de la palabra ésta sea válida. '''

palabrita = {
    "hola": "saludo",
    "adios": "despedida",
    "casa": "lugar donde vives",
    "perro": "animal"
}

def only_one_word(word):
    return len(word.split()) == 1

def view_meaning(word):
    if only_one_word(word):
        word = word.strip().lower()
        return palabrita[word] if word in palabrita else "No existe esa palabra"
    else:
        return "Debe ingresar solo una palabra"

print(view_meaning("casaa de mi mama"))
print(view_meaning("    casa     "))
print(view_meaning("    casaaaaaa     "))


for _, value in palabrita.items():# _ es para no usar la variable
    print(value)
    
#ml ops - machine learning operations
#Arquitecto de datos 
