#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("qual preço do primeiro produto? "))
preco2 = float(input("qual preço do segundo produto? "))
preco3 = float(input("qual preço do terceiro produto? "))

if preco1 < preco2 and preco1 < preco3:
    print("eu quero o primeiro produto")

elif preco2 < preco1 and preco2 < preco3:
    print("eu quero o segundo produto")

elif preco3 < preco2 and preco3 < preco1:
    print("eu quero o terceiro produto")

