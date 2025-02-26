def verificar_contraseña(password, numbers, specials_character, uppercase_letters):
    is_number_found = False
    is_special_character_found = False
    is_uppercase_found = False

    for number in numbers:
        if number in password:
            is_number_found = True
            break

    for especial in specials_character:
        if especial in password:
            is_special_character_found = True
            break

    for letter in uppercase_letters:
        if letter in password:
            is_uppercase_found = True
            break

    return is_number_found, is_special_character_found, is_uppercase_found


numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
specials_character = ["+", "/", "@", "#", "$", "%", "&", "*", "!", "?"]
dictionary_of_uppercase_letters = {
    "uppercase_letters": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
}

while True:
    password_name = input("Ingrese su contraseña: ")
    is_number_found, is_special_character_found, is_uppercase_found = verificar_contraseña(
        password_name, numbers, specials_character, dictionary_of_uppercase_letters[
            "uppercase_letters"]
    )

    if is_number_found and is_special_character_found and is_uppercase_found:
        print("Tu contraseña es correcta.")
        break
    else:
        if not is_number_found:
            print("No te olvides de colocar un número.")
        if not is_special_character_found:
            print("No te olvides de colocar un caracter especial.")
        if not is_uppercase_found:
            print("No te olvides de colocar una mayúscula.")
