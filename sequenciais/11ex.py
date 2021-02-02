#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

numero1_int = int(input("digite o primeiro inteiro: "))
numero2_int = int(input("digite o segundo inteiro: "))
numero_real = float(input("digite o numero real: "))

print("\no produto do primeiro com metade do segundo é: ",(numero1_int * 2) * (numero2_int / 2))
print("\na soma do triplo do primeiro com o terceiro é: ",(numero1_int * 3) + numero2_int)
print(f"\no terceiro elevado ao cubo é: {(numero_real ** 3):.2f}")