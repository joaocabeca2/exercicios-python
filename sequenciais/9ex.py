#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9)

temperatura = int(input("qual a temperatura de agora? "))

temperatura_em_celsius = 5 * ((temperatura - 32) / 9)

print("a temperatura em celsius é", temperatura_em_celsius)