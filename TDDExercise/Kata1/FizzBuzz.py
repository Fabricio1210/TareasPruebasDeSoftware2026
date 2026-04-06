def fizzbuzz(num) -> str:
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return f"{num}"
