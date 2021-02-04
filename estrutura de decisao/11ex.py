#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("qual seu salario? "))

if salario <= 280:
    print("o reajuste foi de 20%, seu novo slário é de ", (20 / 100 * salario) + salario)

elif salario > 280 and salario <= 700:
    print("o reajuste foi de 15%, seu novo de salario é de", (15 / 100 * salario) + salario)

elif salario > 700 and salario <= 1500:
    print("reajuste de 10%, seu novo salario é de", (10 / 100 * salario) + salario)

elif salario > 1500:
    print("reajuste de 5%, seu novo salario é de:", (5 / 100 * salario) + salario)