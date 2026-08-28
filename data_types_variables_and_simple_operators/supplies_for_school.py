pens_packages = int(input())
markers_packages = int(input())
cleaner_liters = int(input())
discount_percent = int(input())

total_price = (
    pens_packages * 5.80 +
    markers_packages * 7.20 +
    cleaner_liters * 1.20
)

discount = total_price * discount_percent / 100

final_price = total_price - discount

print(final_price)
