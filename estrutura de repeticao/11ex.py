#Altere o programa anterior para mostrar no final a soma dos números.

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
soma = 0

for indice in range(numero1+1, numero2):
    print(indice, end = " ")
    soma += indice
print(f"\na soma é {soma}")