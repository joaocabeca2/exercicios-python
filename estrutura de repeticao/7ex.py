#Faça um programa que leia 5 números e informe o maior número.

numero_maior = 0

for indice in range(5):
    numero = int(input("digite um numero: "))

    if numero_maior < numero:
        numero_maior = numero

print("\no maior numero é ",numero_maior)