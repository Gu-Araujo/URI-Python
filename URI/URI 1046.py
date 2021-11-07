inic, fim = map(int, input().split())

if inic > fim:
    print("O JOGO DUROU {} HORA(S)".format(24 - (inic - fim)))
elif fim > inic:
    print("O JOGO DUROU {} HORA(S)".format(fim - inic))
elif inic == fim:
    print("O JOGO DUROU 24 HORA(S)")
