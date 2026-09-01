a = float(input())
b = float(input())
c = float(input())

if a == 0 or b == 0 or c == 0:
    print('zero')
else:
    negative_count = 0

    if a < 0:
        negative_count += 1
    if b < 0:
        negative_count += 1
    if c < 0:
        negative_count += 1

    if negative_count % 2 == 0:
        print('positive')
    else:
        print('negative')