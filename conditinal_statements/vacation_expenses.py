season = input()
accommodation = input()
days = int(input())

price_per_night = 0
discount = 0

if season == 'Spring':
    discount = 0.20
    if accommodation == 'Hotel':
        price_per_night = 30
    else:
        price_per_night = 10

elif season == 'Summer':
    if accommodation == 'Hotel':
        price_per_night = 50
    else:
        price_per_night = 30

elif season == 'Autumn':
    discount = 0.30
    if accommodation == 'Hotel':
        price_per_night = 20
    else:
        price_per_night = 15

elif season == 'Winter':
    discount = 0.10
    if accommodation == 'Hotel':
        price_per_night = 40
    else:
        price_per_night = 10

current_price = price_per_night * days
total_price = current_price - (current_price * discount)
print(f'{total_price:.2f}')
