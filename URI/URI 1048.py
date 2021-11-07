salario = float(input())

if 0 < salario <= 400:
    nsalario = salario + ((salario * 15)/100)
    reaj = 15
    print("Novo salario: %.2f" % nsalario)
    print("Reajuste ganho: %.2f" % (nsalario - salario))
    print("Em percentual: " + str(reaj) + " %")

elif 400 < salario <= 800:
    nsalario = salario + ((salario * 12)/100)
    reaj = 12
    print("Novo salario: %.2f" % nsalario)
    print("Reajuste ganho: %.2f" % (nsalario - salario))
    print("Em percentual: " + str(reaj) + " %")

elif 800 < salario <= 1200:
    nsalario = salario + ((salario * 10)/100)
    reaj = 10
    print("Novo salario: %.2f" % nsalario)
    print("Reajuste ganho: %.2f" % (nsalario - salario))
    print("Em percentual: " + str(reaj) + " %")

elif 1200 < salario <= 2000:
    nsalario = salario + ((salario * 7)/100)
    reaj = 7
    print("Novo salario: %.2f" % nsalario)
    print("Reajuste ganho: %.2f" % (nsalario - salario))
    print("Em percentual: " + str(reaj) + " %")

else:
    nsalario = salario + ((salario * 4)/100)
    reaj = 4
    print("Novo salario: %.2f" % nsalario)
    print("Reajuste ganho: %.2f" % (nsalario - salario))
    print("Em percentual: " + str(reaj) + " %")
