#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

fatorial = []
numero = int(input("digite um numero: "))
multi = 1

for indice in range(numero):
    fatorial.append(indice+1)
    multi *= indice+1

print(sorted(fatorial, reverse = True), "= ", multi)
