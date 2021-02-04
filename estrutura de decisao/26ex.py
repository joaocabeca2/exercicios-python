#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

tipo = str(input("tipo de combustivel "))
litros = int(input("quantidade de litros: "))

if tipo == "alcool" and litros <= 20:
    print("combustivel: gasolina\n com", litros, "litros voce tem 3% de desconto e o preço será: ", 1.9 * litros - (3 / 100 * 1.9*litros))

elif tipo == "alcool" and litros > 20:
    print("combustivel: gasolina\n com", litros, "litros voce tem 5% de desconto e o preço será: ", 1.9 * litros - (5 / 100 * 1.9*litros))

elif tipo == "gasolina" and litros <= 20:
    print("combustivel: gasolina\n com", litros, "litros voce tem 4% de desconto e o preço será: ", 2.5 * litros - (4 / 100 * 2.5*litros))

elif tipo == "gasolina" and litros > 20:
    print("combustivel: gasolina\n com", litros, "litros voce tem 6% de desconto e o preço será: ", 2.5 * litros - (6 / 100 * 2.5*litros))



