#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = int(input("qual o tamanho da area a ser pintada? "))

litros_tinta = area / 3

latas_tinta  = litros_tinta / 18
print(f"\n vão ser necessarias {latas_tinta:.0f} latas de tinta e vai custar R${latas_tinta * 80:.0f}") 
