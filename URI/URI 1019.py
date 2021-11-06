tempo = int(input())
hora = minuto = 0

if int(tempo/3600) >= 1:
    hora = int(tempo/3600)
    tempo -= hora*3600

if int(tempo/60) >= 1:
    minuto = int(tempo/60)
    tempo -= minuto*60

print("{}:{}:{}".format(hora, minuto, tempo))
