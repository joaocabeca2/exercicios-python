#Supondo que a população de um país A seja da ordem de 80000 habitantes 
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a 
# população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_a = 80000
populacao_b = 200000
ano = 0

while populacao_a <= populacao_b:
    populacao_a += (3 / 100 * populacao_a)
    populacao_b += (1.5 / 100 * populacao_b)
    ano += 1

print(f"a população do pais A demorou {ano} anos para ultrapassar a população do pais B")
    