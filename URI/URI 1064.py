pos = 0
tot = 0.00
for i in range(0, 6):
    num = float(input())
    if num > 0:
        pos += 1
        tot += num

print(f"{pos} valores positivos")
print("%.1f" % (tot/pos))
