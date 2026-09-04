number = int(input())

biggest_number = float('-inf')

for _ in range(number):
    current_number = int(input())

    if current_number > biggest_number:
        biggest_number = current_number


print(biggest_number)