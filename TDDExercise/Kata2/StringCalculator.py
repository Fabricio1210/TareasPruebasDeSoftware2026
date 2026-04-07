def add(cadena) -> int:
    delimiter = cadena[cadena.rfind("/")+1:cadena.find("\n")]
    cadena = cadena[cadena.find("\n")+1:]
    splitArray = cadena.split(delimiter, -1)
    #this method ensures any length is processed
    result = 0

    if cadena.endswith(","):
        raise ValueError("Weonazo terminala bien")

    for n in splitArray:
        if n == "":
            n = 0
        result += int(n)
    return result
