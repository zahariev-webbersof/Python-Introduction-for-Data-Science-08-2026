available_balance = 0

while True:
    command = input()

    if command == 'End':
        break

    amount = float(command)

    if amount >= 0:
        print(f"Increase: {amount:.2f}")
    else:
        print(f'Decrease: {abs(amount):.2f}')

    available_balance += amount


print(f'Balance: {available_balance:.2f}')