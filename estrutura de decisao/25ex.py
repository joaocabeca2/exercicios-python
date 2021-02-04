#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
#Caso contrário, ele será classificado como "Inocente".

suspeito = 0
resposta = input("telefenou para a vitima?")
if resposta == "sim":
    suspeito += 1

resposta = input("esteve no local do prime?")
if resposta == "sim":
    suspeito += 1

resposta = input("mora perto da vitima?")
if resposta == "sim":
    suspeito += 1

resposta = input("devia para a vitima?")
if resposta == "sim":
    suspeito += 1

resposta = input("ja trabalhou com a vitima?")
if resposta == "sim":
    suspeito += 1

if suspeito == 2:
    print("suspeito")

elif suspeito >= 3 and suspeito <= 4:
    print("cumplice")

elif suspeito == 5:
    print("assassino")

else:
    print("inocente")

