n = int(input())
par = []
impar = []

for x in range(n):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

par.sort()
impar.sort(reverse=True)

for p in par:
    print(p)
for i in impar:
    print(i)
