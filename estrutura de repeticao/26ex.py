#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = 0
candidato2 = 0
candidato3 = 0

eleitores = int(input("numeros de eleitores: "))

for indice in range (eleitores):

    voto = str(input("\nseu voto vai para qual candidato? \n[1]candidato1\n[2]candidato2\n[3]candidato3\n"))

    if voto == "1":
        candidato1 += 1

    elif voto == "2":
        candidato2 += 1

    elif voto == "3":
        candidato3 += 1
print(f"o candidato[1] ficou com {candidato1} votos, o candidato[2] ficou com {candidato2} votos e o candidato[3] ficou com {candidato3} votos")

