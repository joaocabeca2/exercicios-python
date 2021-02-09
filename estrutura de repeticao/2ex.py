#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

senha = ""
nome = ""
while senha == nome:

    nome = str(input("digite seu nome: "))
    senha = str (input("digite sua senha: "))

    if senha == nome:
        print("\ndigite um nome diferente da senha\n")

