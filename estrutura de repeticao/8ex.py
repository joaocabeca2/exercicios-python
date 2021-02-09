#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for indice in range(5):
    numero = int(input("digite um numero: "))
    soma += numero

media = soma / 5
print(f"a soma de todos os numero é {soma} e a media é {media}")