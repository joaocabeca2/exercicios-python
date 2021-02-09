#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = ""
idade = -1
salario = -1
sexo = ""
estado_civil = ""

while len(nome) < 3:
    nome = str(input("digite seu nome: "))

while idade < 0 or idade > 150:
    idade = int(input("\ndigite sua idade: "))

while salario < 0:    
    salario = int(input("\ndigite seu salario: "))

while sexo != "masculino" and sexo != "feminino":
    sexo = str(input("\ndigite seu sexo: "))

while estado_civil != "solteiro" and estado_civil != "casado" and estado_civil != "viuvo" and estado_civil != "divorciado":    
    estado_civil = str(input("\ndigite seu estado civil: "))