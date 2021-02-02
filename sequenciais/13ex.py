#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("qual sua altura? "))

print(f"\no peso ideal para um homem com essa altura é de: {72.7 * altura - 58:.2f}")
print(f"\no peso ideal para uma mulher com essa altura é de: {62.1 * altura - 44.7:.2f}")