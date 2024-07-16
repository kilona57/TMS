def roman_to_int(s: int) -> int:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for char in s[::-1]:
        current_value = roman_values[char]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value

    return result


print(roman_to_int('III'))
print(roman_to_int('IV'))
print(roman_to_int('IX'))
print(roman_to_int('LVIII'))
print(roman_to_int('MCMXCIV'))
