#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input("valor de a: "))

if a == 0:
    print("a equação não é do segundo grau")

else:
    b = int(input("valor de b: "))
    c = int(input("valor de c: "))

delta = b**2 - 4*a*c

raiz1 = (-b - delta**0.5) / 2*a
raiz2 = (-b + delta**0.5) / 2*a

if delta < 0:
    print("a equação não possui raizes")

elif delta == 0:
    print("tem uma raiz de valor:", -b / 2*a)

elif delta > 0:
    print("tem duas raizes: ", raiz1, "e", raiz2)
