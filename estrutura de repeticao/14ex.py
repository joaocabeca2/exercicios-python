#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

par = 0
impar = 0

for indice in range(10):
    numero = int(input("digite um numero: "))

    if numero%2 == 0:
        par += 1
    
    else:
        impar += 1

print(f"nesses 10 numeros {par} são pares e {impar} são impares")
