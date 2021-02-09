#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cds = int(input("quantidade de cds: "))
valor = []

for indice in range(cds):
    valor.append(int(input(f"qual valor do {indice}º cd? ")))

print(f"o valor total investido em cds foi de {sum(valor)} reais e o valor médio gasto em cada um foi de {sum(valor) / cds}")