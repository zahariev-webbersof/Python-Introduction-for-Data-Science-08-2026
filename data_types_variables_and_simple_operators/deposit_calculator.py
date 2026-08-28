# amount = deposited amount + term of deposit * (deposited amount * annual interest rate) / 12

deposit_amount = float(input())
months = int(input())
annual_interest_rate = float(input())

interest = months * (deposit_amount * annual_interest_rate / 100) / 12

final_amount = deposit_amount + interest

print(final_amount)