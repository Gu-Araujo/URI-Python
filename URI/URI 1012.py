valor = input().split(" ")
a, b, c = valor
pi = 3.14159

trang = (float(a) * float(c))/2
circb = (pi * (float(c)**2))
trap = ((float(a) + float(b))*float(c))/2
quad = float(b)**2
ret = float(a) * float(b)

print("TRIANGULO: %.3f" % trang)
print("CIRCULO: %.3f" % circb)
print("TRAPEZIO: %.3f" % trap)
print("QUADRADO: %.3f" % quad)
print("RETANGULO: %.3f" % ret)
