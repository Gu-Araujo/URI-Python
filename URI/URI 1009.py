nome = input()
salario = input()
venda = input()
bonus = float(venda) * 0.15
total = bonus + float(salario)
print("TOTAL = R$ %0.2f" % total)
