nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

# допълнителни материали
nylon += 2
paint += paint * 0.10

# ЦЕНИ на материали
nylon_cost = nylon * 1.50
paint_cost = paint * 14.50
thinner_cost = thinner * 5.00
bags_cost = 0.40

materials_cost = nylon_cost + paint_cost + thinner_cost + bags_cost

# Цена за майстори
craftsmen_cost = materials_cost * 0.30 * hours

total_costs = materials_cost + craftsmen_cost

print(total_costs)
