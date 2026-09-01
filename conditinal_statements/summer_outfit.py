temperature = int(input())
time_of_day = input()

clothing = ''
shoes = ''

if 10 <= temperature <= 18:
    if time_of_day == 'Morning':
        clothing = 'Sweatshirt'
        shoes = 'Sneakers'
    elif time_of_day == 'Afternoon':
        clothing = 'Shirt'
        shoes = 'Moccasins'
    elif time_of_day == 'Evening':
        clothing = 'Shirt'
        shoes = 'Moccasins'

elif 18 < temperature <= 24:
    if time_of_day == 'Morning':
        clothing = 'Shirt'
        shoes = 'Moccasins'
    elif time_of_day == 'Afternoon':
        clothing = 'T-Shirt'
        shoes = 'Sandals'
    elif time_of_day == 'Evening':
        clothing = 'Shirt'
        shoes = 'Moccasins'

else:
    if time_of_day == 'Morning':
        clothing = 'T-Shirt'
        shoes = 'Sandals'
    elif time_of_day == 'Afternoon':
        clothing = 'Swim Suit'
        shoes = 'Barefoot'
    elif time_of_day == 'Evening':
        clothing = 'Shirt'
        shoes = 'Moccasins'


print(f'It\'s {temperature} degrees, get your {clothing} and {shoes}.')
