import time

horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

tempo = horas * 3600 + minutos * 60 + segundos

while tempo >= 0:

    horas = tempo // 3600
    minutos = (tempo % 3600) // 60
    segundos = tempo % 60

    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

    time.sleep(1)

    tempo -= 1

print("TEMPO ESGOTADO!")
