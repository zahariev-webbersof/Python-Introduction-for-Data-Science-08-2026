stop_number = int(input())

current_number = int(input())

while current_number != stop_number:
    previous_number = current_number
    current_number = int(input())

bonus = previous_number * 1.20

print(int(bonus))