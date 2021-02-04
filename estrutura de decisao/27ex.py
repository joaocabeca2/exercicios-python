#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
#  receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente

morango_kg = int(input("quantidade de kg em morangos: "))

if morango_kg <= 5:
    preco_morango = 2.5 * morango_kg

else:
    preco_morango = 2.2 * morango_kg

maca_kg = int(input("quantidade de kg em maças: "))

if maca_kg <= 5:
    preco_maca = 1.8 * maca_kg

else:
    preco_maca = 1.5 * maca_kg

if morango_kg + maca_kg > 8 or preco_morango + preco_maca > 25:
    print("o preço final será de ",preco_morango + preco_maca - (10 / 100 * (preco_morango + preco_maca)),"reais")

else:
    print(f"preço morangos: {preco_morango} reais\npreço maça: {preco_maca}reais")
