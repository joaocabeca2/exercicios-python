#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("digite um numero: "))
fatorial = []

for indice in range(1,numero+1):
    fatorial.append(indice)

print(sorted(fatorial, reverse = True))
