#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numero = []

for indice in range(5):
    numero.append(int(input("digite um numeros: ")))
    
print(f"o maior numero é {max(numero)}, o menor numero é {min(numero)} e a soma é {sum(numero)}")
    
    