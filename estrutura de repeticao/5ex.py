#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacao_a = int(input("\ndigite a populaçao do pais A: "))
taxa_a = float(input("\ntaxa de crescimento do pais A: "))
populacao_b = int(input("\ndigite a populaçao do pais B: "))
taxa_b = float(input("\ntaxa de crescimento do pais B: "))
ano = 0

while populacao_a <= populacao_b:
    populacao_a += (taxa_a / 100 * populacao_a)
    populacao_b += (taxa_b / 100 * populacao_b)
    ano += 1

print(f"\na população do pais A demorou {ano} anos para ultrapassar a população do pais B")
    