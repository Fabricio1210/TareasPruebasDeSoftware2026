def passwordValidation(password) -> bool:
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    numeros_encontrados = 0
    tiene_mayuscula = False
    tiene_especial = False
    
    for caracter in password:
        if caracter.isdigit():
            numeros_encontrados += 1
        if caracter.isupper():
            tiene_mayuscula = True
        if not caracter.isalnum():
            tiene_especial = True

    if numeros_encontrados < 2:
        errors.append("The password must contain at least 2 numbers")
    
    if not tiene_mayuscula:
        errors.append("password must contain at least one capital letter")

    if not tiene_especial:
        errors.append("password must contain at least one special character")

    if errors:
        print("\n".join(errors))
        return False

    return True