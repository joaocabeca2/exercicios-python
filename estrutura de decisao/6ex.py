#Faça um Programa que leia três números e mostre o maior deles.

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
numero3 = int(input("digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"o {numero1} é o maior")

elif numero2 > numero1 and numero2 > numero3:
    print(f"o {numero2} é o maior")

elif numero3 > numero1 and numero3 > numero2:
    print(f"o {numero3} é o maior")
