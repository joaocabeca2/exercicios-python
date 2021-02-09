#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, 
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperatura = []

for indice in range(5):
    temperatura.append(int(input("qual o valor da temperatura? ")))

print(f"a temperatura máxima registrada foi de {max(temperatura)}º, a menor temperatura registrada foi de {min(temperatura)}º e a media delas foi de {sum(temperatura) / len(temperatura)}º")
