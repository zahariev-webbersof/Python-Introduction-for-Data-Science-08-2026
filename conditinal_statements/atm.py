balance = int(input())
withdraw = int(input())
limit = int(input())

if withdraw > limit:
    print('The limit was exceeded.')
elif withdraw > balance:
    print('Insufficient availability.')
else:
    print('The withdraw was successful.')