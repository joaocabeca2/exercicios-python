#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível

numero = int(input("digite um numero: "))
primo = 0
divisiveis = []

for indice in range(numero):
    if numero % (indice+1) == 0:
        primo += 1
        divisiveis.append(indice+1)

if primo == 2:
    print("primo")
else:
    print("\nnão é primo e é divisivel por", divisiveis)