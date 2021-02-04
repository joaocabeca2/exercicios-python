#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

operacao = int(input(f"qual operação voce deseja fazer?\n[1] adição\n[2] subtração\n[3] multiplicação\n[4] divisão\n"))

if operacao == 1:
    calculo = numero1 + numero2

elif operacao == 2:
    calculo = numero1 - numero2

elif operacao == 3:
    calculo = numero1 * numero2

elif operacao == 4:
    calculo = numero1 / numero2

if calculo % 2 == 0:
    print("o", calculo, "é par")

else:
    print("o", calculo, "é impar")

if calculo < 0:
    print(f"{calculo} é um numero negativo")

else:
    print(f"{calculo} é positivo")

if calculo == round(calculo):
    print(f"{calculo} é inteiro")
    
else:
    print(f"{calculo} é decimal")