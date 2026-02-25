# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from WhiteBoxExecises import check_number_status, validate_password, calculate_total_discount, calculate_order_total, calculate_items_shipping_cost, validate_login, verify_age, categorize_product, validate_email, celsius_to_fahrenheit, validate_credit_card, validate_date, check_flight_eligibility, validate_url, calculate_quantity_discount, check_file_size, check_loan_eligibility, calculate_shipping_cost, grade_quiz, authenticate_user, get_weather_advisory


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    # EJERCICIO 1
    def test_number_is_positive(self):
        """
        Checks if a number is positive.
        """
        self.assertEqual(check_number_status(7), "Positive")

    def test_number_is_negative(self):
        """
        Checks if a number is negative.
        """
        self.assertEqual(check_number_status(-10), "Negative")      
    
    def test_number_is_zero(self):
        """
        Checks if a number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_number_is_positive_float(self):
        """
        Checks if a number is positiv float.
        """
        self.assertEqual(check_number_status(3.4), "Positive")

    def test_number_is_negative_float(self):
        """
        Checks if a number is negative float.
        """
        self.assertEqual(check_number_status(-8.1), "Negative")

    # EJERCICIO 2
    def test_valid_password(self):
        """
        Checks if the string is a valid password.
        """
        self.assertTrue(validate_password("Password1!"))

    def test_invalid_password_non_especial_character(self):
        """
        Checks if the string is a invalid password does not content a special character.
        """
        self.assertFalse(validate_password("MatuteRemus90"))
    
    def test_invalid_password_non_number(self):
        """
        Checks if the string is a invalid password does not content a number.
        """
        self.assertFalse(validate_password("Juanito#"))
    
    def test_invalid_password_non_number(self):
        """
        Checks if the string is a invalid password does not content a number.
        """
        self.assertFalse(validate_password("Juanito#"))

    def test_invalid_password_non_uppercase_character(self):
        """
        Checks if the string is a invalid password does not content an uppercase character.
        """
        self.assertFalse(validate_password("terreneitor70&"))
    
    def test_invalid_password_with_no_correct_length(self):
        """
        Checks if the string is a invalid password does not have the correct length.
        """
        self.assertFalse(validate_password("tie12$S"))

    def test_valid_password_with_especial_character_1(self):
        """
        Checks if the string is a valid with the character !.
        """
        self.assertTrue(validate_password("SecurePassword1210!"))
    
    def test_valid_password_with_especial_character_2(self):
        """
        Checks if the string is a valid with the character @.
        """
        self.assertTrue(validate_password("SecurePassword1210@"))

    def test_valid_password_with_especial_character_3(self):
        """
        Checks if the string is a valid with the character #.
        """
        self.assertTrue(validate_password("SecurePassword1210#"))

    def test_valid_password_with_especial_character_4(self):
        """
        Checks if the string is a valid with the character $.
        """
        self.assertTrue(validate_password("SecurePassword1210$"))

    def test_valid_password_with_especial_character_5(self):
        """
        Checks if the string is a valid with the character %.
        """
        self.assertTrue(validate_password("SecurePassword1210%"))

    def test_valid_password_with_especial_character_6(self):
        """
        Checks if the string is a valid with the character &.
        """
        self.assertTrue(validate_password("SecurePassword1210&")) 

    # EJERCICIO 3
    def test_no_discount_low_amount(self):
        """
        Checks if a total amount less than 100 has 0 discount.
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_no_discount_boundary(self):
        """
        Checks the boundary: 99.99 should still have 0 discount.
        """
        self.assertEqual(calculate_total_discount(99.99), 0)

    def test_discount_10_percent_lower_boundary(self):
        """
        Checks if exactly 100 receives 10% discount (10.0).
        """
        self.assertEqual(calculate_total_discount(100), 10.0)

    def test_discount_10_percent_middle(self):
        """
        Checks if an amount in the middle (300) receives 10% discount (30.0).
        """
        self.assertEqual(calculate_total_discount(300), 30.0)

    def test_discount_10_percent_upper_boundary(self):
        """
        Checks if exactly 500 receives 10% discount (50.0).
        """
        self.assertEqual(calculate_total_discount(500), 50.0)

    def test_discount_20_percent_above_500(self):
        """
        Checks if an amount greater than 500 receives 20% discount.
        """
        self.assertEqual(calculate_total_discount(600), 120.0)

    # EJERCICIO 4
    def test_order_no_discount(self):
        """
        Checks order with quantity 5 (no discount).
        """
        items = [{"quantity": 5, "price": 100}]
        self.assertEqual(calculate_order_total(items), 500)

    def test_order_5_percent_min(self):
        """
        Checks lower boundary for 5% discount (quantity 6).
        """
        items = [{"quantity": 6, "price": 100}]
        self.assertAlmostEqual(calculate_order_total(items), 570.0)

    def test_order_5_percent_max(self):
        """
        Checks upper boundary for 5% discount (quantity 10).
        """
        items = [{"quantity": 10, "price": 100}]
        self.assertEqual(calculate_order_total(items), 950.0)

    def test_order_10_percent(self):
        """
        Checks 10% discount (quantity 11).
        """
        items = [{"quantity": 11, "price": 100}]
        self.assertEqual(calculate_order_total(items), 990.0)

    def test_order_mixed_items(self):
        """
        Checks multiple items with different discounts.
        """
        items = [
            {"quantity": 2, "price": 100},
            {"quantity": 10, "price": 100}
        ]
        self.assertEqual(calculate_order_total(items), 1150.0)

    def test_order_empty(self):
        """
        Checks an empty order list.
        """
        items = []
        self.assertEqual(calculate_order_total(items), 0)

    # EJERCICIO 5
    def test_shipping_standard_low(self):
        """
        Checks standard shipping with weight <= 5.
        """
        items = [{"weight": 2}, {"weight": 2}] # Total 4
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_shipping_standard_medium(self):
        """
        Checks standard shipping with weight between 5 and 10.
        """
        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_shipping_standard_high(self):
        """
        Checks standard shipping with weight > 10.
        """
        items = [{"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_shipping_express_low(self):
        """
        Checks express shipping with weight <= 5.
        """
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_shipping_express_high(self):
        """
        Checks express shipping with weight > 10.
        """
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_shipping_invalid_method(self):
        """
        Checks that an invalid shipping method raises ValueError.
        """
        items = [{"weight": 1}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "drone")

    # EJERCICIO 6
    def test_login_success(self):
        """
        Checks successful login with valid lengths.
        """
        self.assertEqual(validate_login("user_test1", "pass_12345"), "Login Successful")

    def test_login_user_too_short(self):
        """
        Checks failure when username is too short (< 5).
        """
        self.assertEqual(validate_login("user", "password123"), "Login Failed")

    def test_login_user_too_long(self):
        """
        Checks failure when username is too long (> 20).
        """
        self.assertEqual(validate_login("a_very_long_username_that_fails", "password123"), "Login Failed")

    def test_login_pass_too_short(self):
        """
        Checks failure when password is too short (< 8).
        """
        self.assertEqual(validate_login("valid_user", "12345"), "Login Failed")

    def test_login_pass_too_long(self):
        """
        Checks failure when password is too long (> 15).
        """
        self.assertEqual(validate_login("valid_user", "this_is_a_very_long_password"), "Login Failed")

    def test_login_boundaries(self):
        """
        Checks the exact boundaries (Username 5, Password 8).
        """
        self.assertEqual(validate_login("abcde", "12345678"), "Login Successful")

    # EJERCICIO 7
    def test_age_eligible_min(self):
        """
        Checks lower boundary for eligibility (18).
        """
        self.assertEqual(verify_age(18), "Eligible")

    def test_age_eligible_max(self):
        """
        Checks upper boundary for eligibility (65).
        """
        self.assertEqual(verify_age(65), "Eligible")

    def test_age_eligible_middle(self):
        """
        Checks a value in the middle of the range (30).
        """
        self.assertEqual(verify_age(30), "Eligible")

    def test_age_not_eligible_young(self):
        """
        Checks failure for age too young (17).
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_not_eligible_old(self):
        """
        Checks failure for age too old (66).
        """
        self.assertEqual(verify_age(66), "Not Eligible")
    
    # EJERCICIO 8
    def test_product_cat_a(self):
        """
        Checks Category A (10 to 50).
        """
        self.assertEqual(categorize_product(25), "Category A")

    def test_product_cat_b(self):
        """
        Checks Category B (51 to 100).
        """
        self.assertEqual(categorize_product(75), "Category B")

    def test_product_cat_c(self):
        """
        Checks Category C (101 to 200).
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_product_cat_d_low(self):
        """
        Checks Category D for prices below 10.
        """
        self.assertEqual(categorize_product(5), "Category D")

    def test_product_cat_d_high(self):
        """
        Checks Category D for prices above 200.
        """
        self.assertEqual(categorize_product(250), "Category D")

    def test_product_gap_case(self):
        """
        Checks the gap between A and B (e.g., 50.5).
        """
        self.assertEqual(categorize_product(50.5), "Category D")

    # EJERCICIO 9
    def test_email_valid(self):
        """
        Checks a perfectly valid email within length limits.
        """
        self.assertEqual(validate_email("test@mail.com"), "Valid Email")

    def test_email_too_short(self):
        """
        Checks failure when email is too short (< 5).
        """
        self.assertEqual(validate_email("a@b."), "Invalid Email")

    def test_email_too_long(self):
        """
        Checks failure when email exceeds 50 characters.
        """
        long_email = "a" * 45 + "@mail.com" # 54 caracteres aprox.
        self.assertEqual(validate_email(long_email), "Invalid Email")

    def test_email_no_at(self):
        """
        Checks failure when the '@' symbol is missing.
        """
        self.assertEqual(validate_email("testmail.com"), "Invalid Email")

    def test_email_no_dot(self):
        """
        Checks failure when the dot '.' is missing.
        """
        self.assertEqual(validate_email("test@mailcom"), "Invalid Email")

    def test_email_boundary_min(self):
        """
        Checks the minimum valid length (5 characters).
        """
        self.assertEqual(validate_email("a@b.c"), "Valid Email")
    
    # EJERCICIO 10
    def test_temp_zero(self):
        """
        Checks the freezing point (0 Celsius).
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_temp_min_boundary(self):
        """
        Checks lower boundary (-100 Celsius).
        """
        self.assertEqual(celsius_to_fahrenheit(-100), -148.0)

    def test_temp_max_boundary(self):
        """
        Checks upper boundary (100 Celsius).
        """
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_temp_invalid_low(self):
        """
        Checks failure for temperature below -100.
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_temp_invalid_high(self):
        """
        Checks failure for temperature above 100.
        """
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

    def test_temp_float_result(self):
        """
        Checks a value that results in a float.
        """
        self.assertEqual(celsius_to_fahrenheit(25), 77.0)
    
    # EJERCICIO 11
    def test_card_valid_min(self):
        """
        Checks minimum valid length (13 digits).
        """
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_card_valid_max(self):
        """
        Checks maximum valid length (16 digits).
        """
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_card_too_short(self):
        """
        Checks failure when length is less than 13.
        """
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_card_too_long(self):
        """
        Checks failure when length is more than 16.
        """
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_card_non_digits(self):
        """
        Checks failure when card contains letters or symbols.
        """
        self.assertEqual(validate_credit_card("123456789012a"), "Invalid Card")

    def test_card_with_spaces(self):
        """
        Checks failure when card contains spaces (isdigit returns False).
        """
        self.assertEqual(validate_credit_card("1234 5678 9012"), "Invalid Card")
    
    # EJERCICIO 12
    def test_date_valid(self):
        """
        Checks a perfectly valid date.
        """
        self.assertEqual(validate_date(2024, 6, 15), "Valid Date")

    def test_date_year_min_boundary(self):
        """
        Checks the lower boundary for year (1900).
        """
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_date_year_max_boundary(self):
        """
        Checks the upper boundary for year (2100).
        """
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_date_invalid_year(self):
        """
        Checks failure for a year out of range (1899).
        """
        self.assertEqual(validate_date(1899, 5, 10), "Invalid Date")

    def test_date_invalid_month(self):
        """
        Checks failure for a month out of range (13).
        """
        self.assertEqual(validate_date(2020, 13, 1), "Invalid Date")

    def test_date_invalid_day(self):
        """
        Checks failure for a day out of range (32).
        """
        self.assertEqual(validate_date(2020, 1, 32), "Invalid Date")

    def test_date_negative_values(self):
        """
        Checks failure with negative values.
        """
        self.assertEqual(validate_date(2020, -1, 10), "Invalid Date")
    
    # EJERCICIO 13
    def test_flight_age_eligible(self):
        """
        Checks eligibility by age (within range) without frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_flight_frequent_flyer_eligible(self):
        """
        Checks eligibility by frequent flyer status, even if age is outside range.
        """
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_flight_both_eligible(self):
        """
        Checks eligibility when both conditions are met.
        """
        self.assertEqual(check_flight_eligibility(25, True), "Eligible to Book")

    def test_flight_not_eligible(self):
        """
        Checks failure when neither condition is met.
        """
        self.assertEqual(check_flight_eligibility(15, False), "Not Eligible to Book")

    def test_flight_age_boundary_min(self):
        """
        Checks the lower age boundary (18).
        """
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_flight_age_boundary_max(self):
        """
        Checks the upper age boundary (65).
        """
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")
    
    # EJERCICIO 14
    def test_url_https_valid(self):
        """
        Checks a standard valid HTTPS URL.
        """
        self.assertEqual(validate_url("https://google.com"), "Valid URL")

    def test_url_http_valid(self):
        """
        Checks a standard valid HTTP URL.
        """
        self.assertEqual(validate_url("http://google.com"), "Valid URL")

    def test_url_too_long_http(self):
        """
        Checks failure for HTTP URL exceeding 255 chars.
        """
        long_url = "http://" + ("a" * 250)
        self.assertEqual(validate_url(long_url), "Invalid URL")

    def test_url_invalid_protocol(self):
        """
        Checks failure for missing or incorrect protocol.
        """
        self.assertEqual(validate_url("ftp://server.com"), "Invalid URL")

    def test_url_no_protocol(self):
        """
        Checks failure for URL without protocol.
        """
        self.assertEqual(validate_url("www.google.com"), "Invalid URL")

    def test_url_boundary_255(self):
        """
        Checks the exact 255 character limit for HTTP.
        """
        url_255 = "http://" + ("a" * 248)
        self.assertEqual(validate_url(url_255), "Valid URL")

    # EJERCICIO 15
    def test_qty_no_discount(self):
        """
        Checks range for no discount (1 to 5).
        """
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_qty_no_discount_boundary(self):
        """
        Checks upper boundary for no discount (5).
        """
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_qty_5_percent_min(self):
        """
        Checks lower boundary for 5% discount (6).
        """
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_qty_5_percent_max(self):
        """
        Checks upper boundary for 5% discount (10).
        """
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_qty_10_percent(self):
        """
        Checks range for 10% discount (above 10).
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    def test_qty_invalid_or_zero(self):
        """
        Checks behavior for quantity 0 or less (returns 10% based on code logic).
        """
        self.assertEqual(calculate_quantity_discount(0), "10% Discount")
    
    # EJERCICIO 16
    def test_file_size_valid(self):
        """
        Checks a middle range valid file size.
        """
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_file_size_min_boundary(self):
        """
        Checks the lower boundary (0 bytes).
        """
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_file_size_max_boundary(self):
        """
        Checks the upper boundary (exactly 1 MB).
        """
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_file_size_too_large(self):
        """
        Checks failure for size slightly above 1 MB.
        """
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    def test_file_size_negative(self):
        """
        Checks failure for negative file size.
        """
        self.assertEqual(check_file_size(-1), "Invalid File Size")
    
    # EJERCICIO 17
    def test_loan_not_eligible(self):
        """
        Checks income below 30,000.
        """
        self.assertEqual(check_loan_eligibility(25000, 800), "Not Eligible")

    def test_loan_standard_mid_income(self):
        """
        Checks income 30k-60k with high credit score (> 700).
        """
        self.assertEqual(check_loan_eligibility(45000, 710), "Standard Loan")

    def test_loan_secured_mid_income(self):
        """
        Checks income 30k-60k with low credit score (<= 700).
        """
        self.assertEqual(check_loan_eligibility(45000, 650), "Secured Loan")

    def test_loan_premium_high_income(self):
        """
        Checks income > 60k with high credit score (> 750).
        """
        self.assertEqual(check_loan_eligibility(70000, 760), "Premium Loan")

    def test_loan_standard_high_income(self):
        """
        Checks income > 60k with moderate credit score (<= 750).
        """
        self.assertEqual(check_loan_eligibility(70000, 720), "Standard Loan")

    def test_loan_income_boundary(self):
        """
        Checks the exact boundary of 30,000.
        """
        self.assertEqual(check_loan_eligibility(30000, 710), "Standard Loan")
    
    def test_loan_income_just_below_30k(self):
        """
        Boundary: 29,999 (Should be Not Eligible).
        """
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_loan_income_boundary_60k(self):
        """
        Boundary: 60,000 (Exactly high end of Standard/Secured).
        """
        self.assertEqual(check_loan_eligibility(60000, 750), "Standard Loan")

    def test_loan_income_just_above_60k(self):
        """
        Boundary: 60,001 (Should jump to Premium/Standard logic).
        """
        self.assertEqual(check_loan_eligibility(60001, 751), "Premium Loan")

    def test_loan_credit_score_boundary_700(self):
        """
        Boundary: 700 (Credit score is > 700, so 700 should be Secured).
        """
        self.assertEqual(check_loan_eligibility(40000, 700), "Secured Loan")

    def test_loan_credit_score_boundary_750(self):
        """
        Boundary: 750 (Credit score is > 750, so 750 should be Standard).
        """
        self.assertEqual(check_loan_eligibility(70000, 750), "Standard Loan")
    
    # EJERCICIO 18
    def test_ship_small_all_min(self):
        """
        Path 1: All dimensions within small package limits (Cost 5).
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_ship_medium_all_min(self):
        """
        Path 2: All dimensions within medium package limits (Cost 10).
        """
        self.assertEqual(calculate_shipping_cost(2, 15, 15, 15), 10)

    def test_ship_large_weight(self):
        """
        Path 3: Weight exceeds medium limit (Cost 20).
        """
        self.assertEqual(calculate_shipping_cost(6, 15, 15, 15), 20)

    def test_ship_large_length(self):
        """
        Boundary: Length exceeds medium limit (Cost 20).
        """
        self.assertEqual(calculate_shipping_cost(2, 31, 15, 15), 20)

    def test_ship_gap_dimensions(self):
        """
        Boundary: 10.5 is NOT <= 10 AND NOT >= 11.
        This confirms the 'gap' in the dimension logic.
        """
        self.assertEqual(calculate_shipping_cost(0.5, 10.5, 10, 10), 20)

    def test_ship_weight_just_above_1(self):
        """
        Correction: 1.01 IS > 1, so it enters the Medium category.
        """
        self.assertEqual(calculate_shipping_cost(1.01, 15, 15, 15), 10)

    def test_ship_gap_dimensions(self):
        """
        Gap Analysis: Dimensions between 10 and 11.
        Your code has a 'hole' between 10 and 11 (e.g., 10.5).
        """
        self.assertEqual(calculate_shipping_cost(0.5, 10.5, 10, 10), 20)

    def test_ship_mixed_small_medium(self):
        """
        Logic Test: Small weight but medium dimensions.
        Must return 20 because it doesn't fit either specific Path 1 or 2.
        """
        self.assertEqual(calculate_shipping_cost(0.5, 20, 20, 20), 20)
    
    # EJERCICIO 19
    def test_quiz_pass_min(self):
        """
        Boundary: Minimum requirements for Pass (7 correct, 2 incorrect).
        """
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_quiz_pass_excellent(self):
        """
        Path: Way above requirements (10 correct, 0 incorrect).
        """
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_quiz_conditional_min(self):
        """
        Boundary: Minimum for Conditional Pass (5 correct, 3 incorrect).
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_quiz_conditional_edge(self):
        """
        Boundary: 6 correct and 3 incorrect (Still Conditional).
        """
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")

    def test_quiz_fail_by_correct(self):
        """
        Boundary: Too few correct answers (4 correct, 0 incorrect).
        """
        self.assertEqual(grade_quiz(4, 0), "Fail")

    def test_quiz_fail_by_incorrect(self):
        """
        Boundary: Too many incorrect answers (10 correct, 4 incorrect).
        """
        self.assertEqual(grade_quiz(10, 4), "Fail")

    def test_quiz_overlap_priority(self):
        """
        Logic Path: 8 correct, 2 incorrect meets both IFs. 
        Should return "Pass" due to order of execution.
        """
        self.assertEqual(grade_quiz(8, 2), "Pass")
    
    # EJERCICIO 20
    def test_auth_admin_success(self):
        """
        Path 1: Exact match for Admin credentials.
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_auth_user_success_min(self):
        """
        Path 2: Minimum requirements for User (User: 5 chars, Pass: 8 chars).
        """
        self.assertEqual(authenticate_user("user1", "pass1234"), "User")

    def test_auth_user_username_too_short(self):
        """
        Boundary: Username 4 chars (too short), even if password is okay.
        """
        self.assertEqual(authenticate_user("abc1", "password123"), "Invalid")

    def test_auth_user_password_too_short(self):
        """
        Boundary: Password 7 chars (too short), even if username is okay.
        """
        self.assertEqual(authenticate_user("validUser", "1234567"), "Invalid")

    def test_auth_admin_wrong_password(self):
        """
        Logic Path: Username is 'admin' but password is not 'admin123'.
        If it meets User criteria (len >= 8), it should return 'User'.
        """
        self.assertEqual(authenticate_user("admin", "secretPass"), "User")

    def test_auth_empty_fields(self):
        """
        Edge Case: Empty strings.
        """
        self.assertEqual(authenticate_user("", ""), "Invalid")
    
    # EJERCICIO 21
    def test_weather_high_both(self):
        """
        Path 1: Both conditions met (> 30 and > 70).
        """
        self.assertEqual(get_weather_advisory(31, 71), "High Temperature and Humidity. Stay Hydrated.")

    def test_weather_high_temp_only(self):
        """
        Boundary/Logic: Temp > 30 but humidity <= 70.
        Should fall to 'No Specific Advisory'.
        """
        self.assertEqual(get_weather_advisory(35, 70), "No Specific Advisory")

    def test_weather_high_humidity_only(self):
        """
        Boundary/Logic: Humidity > 70 but temp <= 30.
        Should fall to 'No Specific Advisory'.
        """
        self.assertEqual(get_weather_advisory(30, 80), "No Specific Advisory")

    def test_weather_low_temp(self):
        """
        Path 2: Temperature below 0.
        """
        self.assertEqual(get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!")

    def test_weather_low_temp_boundary(self):
        """
        Boundary: Exactly 0.
        Since it's '< 0', 0 should return 'No Specific Advisory'.
        """
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")

    def test_weather_normal(self):
        """
        Path 3: Pleasant weather (no advisories).
        """
        self.assertEqual(get_weather_advisory(20, 40), "No Specific Advisory")

if __name__ == '__main__':
    unittest.main()