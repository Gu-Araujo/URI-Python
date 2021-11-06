valores = input().split()
valores = list(map(float, valores))
X, Y, Z = valores

if (X+Y > Z and Y+Z > X and X+Z > Y):
    print("Perimetro = %.1f" % (X+Y+Z))
else:
    print("Area = %.1f" % (0.5*(X+Y)*Z))
