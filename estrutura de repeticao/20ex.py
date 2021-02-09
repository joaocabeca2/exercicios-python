#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
# o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

continuar = "sim"

while continuar == "sim" or continuar == "s":
    fatorial = []
    valor = int(input("digite um valor: "))

    if valor <= 0 or valor > 16:
        print("digite um valor inteiro positivo menor que 16")
    else:
        for indice in range(valor):
            fatorial.append(indice+1)
        print(sorted(fatorial, reverse = True))
    
    continuar = str(input("quer cntinuar? "))
    continuar = continuar.lower()