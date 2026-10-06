import time

tempo = int(input("Digite o tempo em segundos: "))

while tempo > 0:
    print(tempo)
    time.sleep(1)
    tempo -= 1

print("TEMPO ESGOTADO!")
