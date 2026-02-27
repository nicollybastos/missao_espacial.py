# Agenda 03 - EAD Etec (27/02/2026)

nome = input("Astronauta da missão: ")
distancia = int(input("Distância da viagem (km): "))
velocidade = int(input("Velocidade média (km/h): "))

tempo_horas = distancia / velocidade
tempo_dias = tempo_horas / 24

print("Astronauta %s, bem-vindo à simulação!" % Nome)
print("A viagem terá uma distância de %d km (até a Lua)." % distancia)
print("Com velocidade média de %d km/h, o tempo estimado é:" % velocidade)
print("%.2f" % tempo_horas, "horas (%.2f dias)." % tempo_dias)
print("Boa sorte na missão!")
