# Black Box Test
Es el ejercicio para identificar las diferentes pruebas de caja negra que hay y como utilizarla segun los casos que se meustran a continuacion
## 1. Function that validates credit card numbers.
 - Valid card numbers: Length between 13 and 16 digits, containing only numeric digits.
 ### Tipo de prueba
- Equivalence partitioning
### Test cases
1. input = 3819221409431931
```bash
Expected output = Valid
```
2. input = 7491AOD209616451
```bash
Expected output = Invalid, Characters detected
```
3. input = 74919120
```bash
Expected output = Invalid, Short String
```
4. input = 7491912009317419381381
```bash
Expected output = Invalid, Long String
```
## 2. Function that validates dates.
   - Valid years: Between 1900 and 2100.
   - Valid months: Between 1 and 12.
   - Valid days: Between 1 and 31.

 ### Tipo de prueba
- Equivalence partitioning
### Test cases

1. input = 21/03/2026
```bash
Expected output = Valid
```

2. input = 90/05/1996
```bash
Expected output = Invalid, Day input invalid
```

3. input = 19/13/1965
```bash
Expected output = Invalid, Month input invalid
```

4. input = 29/06/2104
```bash
Expected output = Invalid, Long String
```

## 3. Function that checks the eligibility of a passenger to book a flight.
   - Eligible ages: Between 18 and 65.
   - Frequent flyers: True or False.
 ### Tipo de prueba
- Equivalence partitioning
### Test cases

1. input = {Age = 21, Frequent Flyer = true} 
```bash
Expected output = Valid Entries
```

2. input = {Age = 16, Frequent Flyer = true} 
```bash
Expected output = Invalid, Age out of range
```

3. input = {Age = 71, Frequent Flyer = true} 
```bash
Expected output = Invalid, Age out of range
```

4. input = {Age = 27, Frequent Flyer = False} 
```bash
Expected output = Invalid, Frequent Flyer is not 'true' 
```

## 4. Function that validates URLs.
   - Valid URLs: Length less than or equal to 255, starting with "http://" or "https://".
 ### Tipo de prueba
- Equivalence partitioning
### Test cases
1. input = http://facebook.com
```bash
Expected output = Valid URL 
```
2. input = https://youtube.com
```bash
Expected output = Valid URL 
```
3. input = ht://x.com
```bash
Expected output = Invalid URL, incorrect prefix 
```
4. input = http://facebookijdiasjdiasjdsjdkakskdkjksjkjakisksksksksksksksksjdaoijdjksjdkjskdjkdkajdkjkjdkjkjkyyyndnndndndndnndndndkdhjshdjsjkahsjdjksahjajhshbhdbhsdhshdhbdansndbsndbnasdnasds,dakuednmdskdjksdjkaksdkjsdjksa.sidjjkdjdalkdjajsdnd,asmdd,md,msdndmema,kkkskdskdkllksdslahjsdbbsb.com
```bash
Expected output = Invalid URL, Invalid URL lenght
```

## 5. Function that calculates the eligibility of a person for a loan based on their income and credit score.
   The eligibility rules are as follows:
   - If the income is less than $30,000, the person is not eligible for a loan.
   - If the income is between $30,000 and $60,000 (inclusive) and the credit score is above 700, the person is eligible for a standard loan.
   - If the income is between $30,000 and $60,000 (inclusive) and the credit score is below or equal to 700, the person is eligible for a secured loan.
   - If the income is greater than $60,000 and the credit score is above 750, the person is eligible for a premium loan.
   - If the income is greater than $60,000 and the credit score is between 700 and 750 (inclusive), the person is eligible for a standard loan.

 ### Tipo de prueba
- Boundary Value Analysis
### Test cases

1. input = {Income = 29,000 , Credit score =  700} 
```bash
Expected output = Client is not eligible for his incomes
```
2. input = {Income = 30,001 , Credit score =  701} 
```bash
Expected output = Client can acquire a standard loan
```
3. input = {Income = 60,000 , Credit score =  701} 
```bash
Expected output = Client can acquire a standard loan
```
4. input = {Income = 30,001 , Credit score =  700} 
```bash
Expected output = Client can acquire a Secured loan
```
4. input = {Income = 60,000 , Credit score =  700} 
```bash
Expected output = Client can acquire a Secured loan
```
5. input = {Income = 60,001 , Credit score =  751} 
```bash
Expected output = Client can acquire a Premium loan
```
6. input = {Income = 60,001 , Credit score =  701} 
```bash
Expected output = Client can acquire a standard loan
```
7. input = {Income = 60,001 , Credit score =  750} 
```bash
Expected output = Client can acquire a standard loan
```
## 6. Function that determines the category of a product in an e-commerce system based on its price.
   The product categories and pricing rules are as follows:
   - Category A: Products priced between $10 and $50 (inclusive).
   - Category B: Products priced between $51 and $100 (inclusive).
   - Category C: Products priced between $101 and $200 (inclusive).
   - Category D: Products priced above $200.
 ### Tipo de prueba
- Boundary Value Analysis
### Test cases
1. input = 11
```bash
Expected output = Category A
```
2. input = 50
```bash
Expected output = Category A
```
3. input = 51
```bash
Expected output = Category B
```
4. input = 100
```bash
Expected output = Category B
```
5. input = 101
```bash
Expected output = Category C
```
6. input = 200
```bash
Expected output = Category C
```
7. input = 201
```bash
Expected output = Category D
```
## 7. Function that calculates the cost of shipping for packages based on their weight and dimensions.
   The shipping cost rules are as follows:
   - If the weight of the package is less than or equal to 1 kg and the dimensions (length, width, and height) are each less than or equal to 10 cm, the cost is $5.
   - If the weight is between 1 and 5 kg (inclusive) and the dimensions are each between 11 and 30 cm (inclusive), the cost is $10.
   - If the weight is greater than 5 kg or any of the dimensions is greater than 30 cm, the cost is $20.
 ### Tipo de prueba
- Boundary Value Analysis
### Test cases

1. input = {Weight = 1 kg , Length, width, and height =  10 cm, 10 cm, 10 cm} 
```bash
Expected output = Cost is $5
```

2. input = {Weight = 1.1 kg , Length, width, and height =  11 cm, 11 cm, 11 cm} 
```bash
Expected output = Cost is $10
```

3. input = {Weight = 1.1 kg , Length, width, and height =  30 cm, 30 cm, 30 cm} 
```bash
Expected output = Cost is $10
```

4. input = {Weight = 5 kg , Length, width, and height =  11 cm, 11 cm, 11 cm} 
```bash
Expected output = Cost is $10
```

5. input = {Weight = 5 kg , Length, width, and height =  30 cm, 30 cm, 30 cm} 
```bash
Expected output = Cost is $10
```

6. input = {Weight = 5.1 kg , Length, width, and height =  31 cm, 31 cm, 31 cm} 
```bash
Expected output = Cost is $20
```

## 8. Create the decision table for a system that provides weather advisories based on temperature and humidity.
   The rules are:
   - Weather recommendation "High temperature and humidity. Stay hydrated." for temperature > 30 and humidity > 70.
   - Weather recommendation "Low temperature. Don't forget your jacket!" for temperature < 0 and any humidity.
   - No weather recommendation for any other temperature and humidity combination.
 ### Tipo de prueba
- Boundary Value Analysis
### Test cases
| Temperature | Humidity | Recommendation |
| :--- | :---: | ---: |
| 31 | 71 | High temperature and humidity. Stay hydrated. |
| -01 | 30 | Low temperature. Don't forget your jacket! |
| 15 | 30 | No weather recommendation. |

## 9. Create the decision table for a system that authenticates users based on their username and password.
   The rules are:
   - Returns "Admin" for username "admin" and password "admin123".
   - Returns "User" for any other username with at least 5 characters and password with at least 8 characters.
   - Returns "Invalid" if the username or password lenghts are not met.

| Username | Password | User type |
| :--- | :---: | ---: |
| admin | admin123 | Admin |
| >=5 | >=8 | User |
| Any other | Any other | Fail |
