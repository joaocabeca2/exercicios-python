#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra_sexo = str(input("digite uma letra para definir seu sexo: "))

letra_sexo = letra_sexo.lower()

if letra_sexo == "m":
    print("é masculino")

elif letra_sexo == "f":
    print("é feminino")

else:
    print("sexo indefinido")