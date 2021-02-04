#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("digite um numero: "))

if numero == 1:
    print("domingo")

elif numero == 2:
    print("segunda")

elif numero == 3:
    print("terça")

elif numero == 4:
    print("quarta")

elif numero == 5:
    print("quinta")

elif numero == 6:
    print("sexta")

elif numero == 7:
    print("sabado")