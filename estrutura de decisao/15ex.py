#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado1 = int(input("valor do primeiro lado: "))
lado2 = int(input("valor do segundo lado: "))
lado3 = int(input("valor do terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("é um triangulo equilatero")

elif lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado3 != lado2 or lado2 == lado3 and lado2 != lado1:
    print("é um triangulo isoceles")

elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("é um traingulo escaleno")
