#Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

if numero1 > numero2:
    print(f"o {numero1} é o maior numero")

elif numero1 < numero2:
    print(f"o {numero2} é o maior numero")

else:
    print("os dois numeros tem o mesmo valor")