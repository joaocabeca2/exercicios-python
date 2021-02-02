#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("qual sua altura? "))

print(f"\nseu peso ideal é: {72.7 * altura - 58:.2f}KG")