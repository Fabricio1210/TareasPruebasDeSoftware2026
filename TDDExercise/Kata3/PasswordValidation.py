def passwordValidation(password) -> bool:
    if len(password) < 8:
        print("Password must be at least 8 characters")
        return False

    return True
