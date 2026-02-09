# Black Box Exercises
Este es la actividad de como identificar los diferentes tipos de prueba estaticas de tabla negra
## 1. Function that checks if a given number is positive, negative, or zero.
### Tipo de prueba
- Equivalence partitioning
### Test cases
1. input = 2
```bash
Expected output = positive
```
2. input = -18
```bash
Expected output = negative
```
3. input = 0
```bash
Expected output = zero
```
4. input = 18.4
```bash
Expected output = positive
```
5. input = -100.2
```bash
Expected output = negative
```
## 2. Function that validates user passwords.
The password validation rules are as follows:

- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, one digit,
and one special character (!, @, #, $, %, or &).

### Tipo de prueba
- Equivalence partitioning

### Test cases
1. input = Anotherdistress1210!
```bash
Expected output = valid
```
2. input = SecurePassword$
```bash
Expected output = invalid, No number found it
```
3. input = "carlos231!"
```bash
Expected output = invalid, No uppercase character found it
```
4. input = s!45D
```bash
Expected output = invalid, length minimum required is 8 characters
```
5. input = "KAMALEO!N19"
```bash
Expected output = invalid, No lower character found it
```
6. input = "Mexico1210"
```bash
Expected output = invalid, No especial character found it('!', '@', '#', '$', '%', '&')  
```
7. input = "Mexico1210!"
```bash
Expected output = valid
```
8. input = "Mexico1210@"
```bash
Expected output = valid
```
9. input = "Mexico1210#"
```bash
Expected output = valid
```
10. input = "Mexico1210$"
```bash
Expected output = valid
```
11. input = "Mexico1210%"
```bash
Expected output = valid
```
12. input = "Mexico1210&"
```bash
Expected output = valid
```
## 3. Function that calculates the discount for a customer's purchase based on the total amount.
The discount rules are as follows:

- If the total amount is less than 100, no discount is applied.
- If the total amount is between 100 and 500 (inclusive), a 10% discount is applied.
- If the total amount is greater than 500, a 20% discount is applied.

### Tipo de prueba
Boundary Value Analysis
### Test cases
1. input = 1
```bash
Expected output = "Discount of 0% applied"
```
2. input = 99
```bash
Expected output = "Discount of 0% applied"
```
3. input = 100
```bash
Expected output = "Discount of 10% applied"
```
4. input = 500
```bash
Expected output = "Discount of 10% applied"
```
5. input = 501
```bash
Expected output = "Discount of 20% applied"
```
## 4. Function that processes user orders in an e-commerce system.
The function calculates the total price of the items in the order,
applying different discounts based on the quantity of each item.
The discount rules are as follows:

- If the quantity of a single item is between 1 and 5 (inclusive), no discount is applied.
- If the quantity of a single item is between 6 and 10 (inclusive), a - 5% discount is applied.
- If the quantity of a single item is greater than 10, a 10% discount - is applied.
### Tipo de prueba
Boundary Value Analysis
### Test cases
1. input = 1
```bash
Expected output = "Discount of 0% applied"
```
2. input = 5
```bash
Expected output = "Discount of 0% applied"
```
3. input = 6
```bash
Expected output = "Discount of 5% applied"
```
4. input = 10
```bash
Expected output = "Discount of 5% applied"
```
5. input = 11
```bash
Expected output = "Discount of 10% applied"
```
## 5. Function that calculates shipping costs for an online shopping system.
The function calculates shipping costs based on the total weight of the items
in the order and the shipping method chosen by the customer.
The shipping cost rules are as follows:

 - For standard shipping:

    - If the total weight is less than or equal to 5 kg, the cost is $10.
    - If the total weight is between 5 and 10 kg (inclusive), the cost is $15.
    - If the total weight is greater than 10 kg, the cost is $20.
- For express shipping:
    - If the total weight is less than or equal to 5 kg, the cost is $20.
    - If the total weight is between 5 and 10 kg (inclusive), the cost is $30.
    - If the total weight is greater than 10 kg, the cost is $40.