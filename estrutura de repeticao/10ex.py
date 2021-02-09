#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

for indice in range(numero1+1, numero2):
    print(indice, end = " ")