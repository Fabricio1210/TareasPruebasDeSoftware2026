def add(cadena) -> int:
    cadena = cadena.replace("\n",",")
    splitArray = cadena.split(",", -1)
    #this method ensures any length is processed
    result = 0
    for n in splitArray:
        if n == "":
            n = 0
        result += int(n)
    return result

print(add("1,2,\n3"))