#Faça um programa que calcule o mostre a média aritmética de N notas.

continuar = "sim"
indice = 0
notas = []

while continuar == "sim" or continuar == "s":
    indice += 1
    notas.append(float(input(f"digite sua nota no {indice} semestre: ")))
    continuar = str(input("\nquer continuar? "))
    continuar = continuar.lower()

print(f"a media em {indice} semestres é {sum(notas) / len(notas)}")

