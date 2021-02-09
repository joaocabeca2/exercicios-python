#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
# Faça um programa que implemente uma caixa registradora rudimentar. 
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
# Um valor zero deve ser informado pelo operador para indicar o final da compra. 
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
# para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
#para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Lojas Tabajara 
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00

valor = 1
indice  = 0
total = 0
produtos = []

while valor != 0:
    indice += 1
    valor = float(input(f"qual valor do {indice}º produto? "))

    if valor != 0:
        produtos.append(valor)
    else:
        break

print(f"Lojas Tabajara:")
for indice in range(len(produtos)):
    print(f"\n{indice+1}º produto: R$ {round(produtos[indice],2)} reais")

dinheiro = float(input("\nvalor do dinheiro fornecido pelo cliente: "))

print(f"total: R$ {sum(produtos)} reais\ndinheiro: R$ {dinheiro} reais\ntroco: R$ {dinheiro - sum(produtos)}")


