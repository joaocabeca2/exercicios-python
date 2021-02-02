#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = int(input("qual o raio do circulo? "))
pi = 3.14

area = pi * raio ** 2
print(f"{area:.1f}m²")