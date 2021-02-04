#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("aprovado com media de", media)

elif media < 7:
    print("reprovado com uma media de", media)

else:
    print("aprovado com distinção com media de", media)
