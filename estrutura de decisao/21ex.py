#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a 
# valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = int(input("digite o valor do saque: "))


if valor_saque >= 10 and valor_saque <= 600:
    
    notas_cem = int(valor_saque / 100)
    numero = valor_saque - notas_cem * 100

    notas_ciquenta = int(numero / 50)
    numero = numero - notas_ciquenta * 50

    notas_dez = int(numero / 10)
    numero = numero - notas_dez * 10

    notas_cinco = int(numero / 5)
    numero = numero - notas_cinco * 5

    notas_um = numero

print(f"para sacar a quantia de {valor_saque}, programa fornece {notas_cem} notas de cem, {notas_ciquenta} de ciquenta, {notas_dez} de dez, {notas_cinco} de cinco e {notas_um} de um real")
