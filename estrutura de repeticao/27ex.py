#Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input("quantidade de turmas no colegio: "))
turma = []

for indice in range (turmas):
    alunos = int(input(f"qual a quantidade de alunos na {indice+1}º turma: "))

    if alunos > 40:
        print("não há turmas com mais de 40 alunos ")
        alunos = int(input(f"\nqual a quantidade de alunos na {indice+1}º turma: "))

    turma.append(alunos)

print(f"a média de alunos por turma é {sum(turma) / len(turma)}")
print(turma)
