n1 = int(input())
n2 = int(input())
operator = input()

result = 0

if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/':
    result = n1 / n2

print(f'{n1} {operator} {n2} = {result:.2f}')