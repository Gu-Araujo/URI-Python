dias = int(input())
ano = dia = 0

if int(dias/365) >= 1:
    ano = int(dias/365)
    dias -= ano*365
if int(dias/30) >= 1:
    dia = int(dias/30)
    dias -= dia*30

print("%d ano(s)" % ano)
print("%d mes(es)" % dia)
print("%d dia(s)" % dias)
