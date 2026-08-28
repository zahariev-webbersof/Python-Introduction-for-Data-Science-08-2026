chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

chicken_price = chicken_menus * 10.35
fish_price = fish_menus * 12.40
vegetarian_price = vegetarian_menus * 8.15

food_price = chicken_price + fish_price + vegetarian_price

dessert_price = food_price * 0.20

delivery_price = 2.5

total_price = food_price + dessert_price + delivery_price

print(total_price)

