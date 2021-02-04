#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
#  Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
#  Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipo_carne = str(input("tipo de carne: "))
quantidade = int(input("quantidade em kg: "))

if tipo_carne == "file duplo" or tipo_carne == "file" or tipo_carne == "f":

    if quantidade <= 5:
        preco = 4.9 * quantidade
    
    else:
        preco = 5.8 * quantidade

elif tipo_carne == "alcatra" or tipo_carne == "a":

    if quantidade <= 5:
        preco = 5.9 * quantidade
    
    else:
        preco = 6.8 * quantidade

elif tipo_carne == "picanha" or tipo_carne == "p":
     
    if quantidade <= 5:
        preco = 6.9 * quantidade
        
    else:
        preco = 7.8 * quantidade

metodo_pagamento = str(input("metodo de pagamento: "))

if metodo_pagamento == "cartao" or metodo_pagamento == "c":
    print(f"voce recebrá um descont de 5% e o preço final será de {preco - (5 / 100 * preco)} reais")

else:
    print("o preço da sua", tipo_carne, "será de ", preco, "reais")

