def passwordValidation(password) -> bool:
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    numeros_encontrados = 0
    for caracter in password:
        if caracter.isdigit():
            numeros_encontrados += 1
            
    if numeros_encontrados < 2:
        errors.append("The password must contain at least 2 numbers")

    if errors:
        print("\n".join(errors))
        return False
    return True