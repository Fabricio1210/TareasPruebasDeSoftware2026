def add(cadena) -> int:
    splitArray = cadena.split(",", -1)
    result = 0
    for n in splitArray:
        result += int(n)
    return result
