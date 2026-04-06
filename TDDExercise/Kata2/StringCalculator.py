def add(cadena) -> int:
    cadena = cadena.replace("\n",",")
    splitArray = cadena.split(",", -1)
    #this method ensures any length is processed
    result = 0

    if cadena.endswith(","):
        raise ValueError("Weonazo terminala bien")

    for n in splitArray:
        if n == "":
            n = 0
        result += int(n)
    return result

print(add("1,2,\n3,"))