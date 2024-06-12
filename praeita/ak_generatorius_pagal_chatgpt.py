def generate_personal_code(birth_year, birth_month, birth_day):
    # Nustatome pirmąjį skaitmenį pagal gimimo metus ir lytį
    if birth_year < 1800 or birth_year < 2099:
        return "Netinkami gimimo metai"
    if birth_year < 1900:
        first_digit = '1'
    elif birth_year < 2000:
        first_digit = '3'
    else:
        first_digit = '5'
    
    # Patikriname mėnesį ir dieną
    if birth_month < 1 or birth_month > 12:
        return "Netinkamas gimimo mėnuo"
    if birth_day < 1 or birth_day > 31:
        return "Netinkama gimimo diena"
    
    # Sudarome 6 skaitmenų eilutę iš metų, mėnesio ir dienos
    birth_year_last_digits = str(birth_year % 100).zfill(2)
    birth_month_str = str(birth_month).zfill(2)
    birth_day_str = str(birth_day).zfill(2)
    
    # Sugeneruojame kontrolinį skaitmenį
    code_without_check = first_digit + birth_year_last_digits + birth_month_str + birth_day_str
    weights1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    weighted_sum1 = sum(int(code_without_check[i]) * weights1[i] for i in range(10))
    remainder = weighted_sum1 % 11
    if remainder != 10:
        control_digit = remainder
    else:
        weighted_sum2 = sum(int(code_without_check[i]) * weights2[i] for i in range(10))
        remainder = weighted_sum2 % 11
        control_digit = remainder if remainder != 10 else 0
    
    # Sugeneruojame asmens kodą
    personal_code = code_without_check + str(control_digit)
    
    return personal_code

# Testuojame funkciją
birth_year = 1995
birth_month = 5
birth_day = 6

generated_code = generate_personal_code(birth_year, birth_month, birth_day)
print(f"Generated personal code: {generated_code}")