def sum_even_odd_digits(number):
    odd_sum = 0
    even_sum = 0

    for digit in str(abs(number)):
        digit = int(digit)

        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


num = int(input())
result = sum_even_odd_digits(num)

print(result)


