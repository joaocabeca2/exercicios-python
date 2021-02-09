#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numero = []

for indice in range(5):
    valor = int(input("digite um numeros: "))

    if valor < 0 or valor > 1000:
        pass
    else:
        numero.append(valor)
    
print(f"o maior numero é {max(numero)}, o menor numero é {min(numero)} e a soma é {sum(numero)}")
    