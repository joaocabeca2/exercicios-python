#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for indice in range(1,50):

    if indice % 2 != 0:
        print(indice, end = " ")
