a, b = map(int, input().split())
total = 0.00

if (a == 1):
    total += (4.00*b)
elif (a == 2):
    total += (4.5*b)
elif (a == 3):
    total += (5.00*b)
elif (a == 4):
    total += (2.00*b)
elif (a == 5):
    total += (1.50*b)

print("Total: R$ %.2f" % total)
