a, b, c = list(map(int, input().split()))
numeros = [a, b, c]
numeros_ord = numeros.copy()
numeros_ord.sort()

for n in range(3):
    print(numeros_ord[n])
print("")
for m in range(3):
    print(numeros[m])
