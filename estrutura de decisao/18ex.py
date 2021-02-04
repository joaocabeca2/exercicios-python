#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input("dia do mes: "))

if dia > 0 and dia <= 31:
    mes = int(input("numero do mes: "))

    if mes > 0 and mes <= 12:
        ano = int(input("ano: "))

        if ano > 999 and ano <= 2022:
            print(f"data: {dia}/{mes}/{ano}")
    else:
        print("mes invalido")

else:
    print("dia do mes ivalido")

