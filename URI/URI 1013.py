valor = input().split(" ")
a, b, c = valor

r1 = (int(a)+int(b)+abs(int(a)-int(b)))/2
r2 = (r1+int(c)+abs(r1-int(c)))/2

print('%d eh o maior' % (r2))
