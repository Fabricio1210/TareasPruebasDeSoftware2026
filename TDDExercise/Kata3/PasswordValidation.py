def passwordValidation(password) -> bool:
    if len(password) < 8:
        print("Password must be at least 8 characters")
        return False
    
    numeros_encontrados = 0
    for caracter in password:
        if caracter.isdigit():
            numeros_encontrados += 1

    if numeros_encontrados < 2:
        print("Password must contain at least 2 numbers")
        return False

    return True
