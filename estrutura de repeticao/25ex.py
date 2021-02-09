#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a 
# média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

continuar = "sim"
indice = 0
idades = []

while continuar == "sim" or continuar == "s":
    indice += 1
    idades.append(int(input(f"digite sua idade: ")))
    continuar = str(input("\nquer continuar? "))
    continuar = continuar.lower()

media = round(sum(idades) / len(idades),2)

if media >= 0 and media <= 25:
    print(f"a media da idade de {indice} pessoas da turma é {media}, uma turma jovem ")

elif media >= 26 and media <= 60:
    print(f"a media da idade de {indice} pessoas da turma é {media}, uma turma adulta ")

elif media > 60:
    print(f"a media da idade de {indice} pessoas da turma é {media}, uma turma idosa ")

