#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("digite primeiro numero: "))
numero2 = int(input("digite segundo numero: "))
numero3 = int(input("digite terceiro numero: "))

if numero1 < numero2 and numero2 < numero3:
    print(numero3, numero2, numero1)

elif numero1 < numero3 and numero3 < numero2:
    print(numero2, numero3, numero1)

elif numero1 > numero2 and numero2 > numero3:
    print(numero1, numero2, numero3)

elif numero1 > numero3 and numero3 > numero2:
    print(numero1, numero3, numero2)

elif numero2 > numero1 and numero1 > numero3:
    print(numero2, numero1, numero3)

elif numero3 > numero1 and numero1 > numero2:
    print(numero3, numero1, numero2)

#é mais facil fazer com loop, mas fazendo um calculo de combinação os resultado possiveis são 6 e assim da para fazer usando of if case



