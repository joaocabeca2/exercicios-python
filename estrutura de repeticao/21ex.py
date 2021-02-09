#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("digite um numero: "))
primo = 0

for indice in range(numero):
    if numero % (indice+1) == 0:
        primo += 1

if primo == 2:
    print("primo")
else:
    print("não é primo")
    
    