def add(cadena) -> int:
    splitArray = cadena.split(",", -1)
    #this method ensures any length is processed
    result = 0
    for n in splitArray:
        result += int(n)
    return result
