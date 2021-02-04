#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
#ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    print(f"o aluno teve notas: {nota1} e {nota2} e ficou com media de {media}, APROVADO COM NOTA A")

if media >= 7.5 and media < 9:
    print(f"o aluno teve notas: {nota1} e {nota2} e ficou com media de {media}, APROVADO COM NOTA B")

if media >= 6 and media < 7.5:
    print(f"o aluno teve notas: {nota1} e {nota2} e ficou com media de {media}, APROVADO COM NOTA C")

if media >= 4 and media < 6:
    print(f"o aluno teve notas: {nota1} e {nota2} e ficou com media de {media}, REPROVADO COM NOTA D")

if media >= 0 and media < 4:
    print(f"o aluno teve notas: {nota1} e {nota2} e ficou com media de {media}, REPROVADO COM NOTA E")    
