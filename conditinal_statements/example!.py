season = input()
accommodation = input()
days = int(input())

prices = {
    'Spring': {'Hotel': 30, 'Camping': 10, 'discount': 0.20},
    'Summer': {'Hotel': 50, 'Camping': 30, 'discount': 0},
    'Autumn': {'Hotel': 20, 'Camping': 15, 'discount': 0.30},
    'Winter': {'Hotel': 40, 'Camping': 10, 'discount': 0.10}
}


price = prices[season][accommodation]
discount = prices[season]['discount']

total_price = price * days * (1 - discount)

print(f'{total_price:.2f}')