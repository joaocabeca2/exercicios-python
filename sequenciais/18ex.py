#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("qual o tamanho do arquivo? "))
velocidade = float(input("qual a velocidade da internet? "))

tempo_download = tamanho_arquivo / velocidade # eu usei como se fosse a forma da velocidade media na física,acredito que esteja certo devido as unidades mostradas

print("o tempo de download em minutos é de: ",tempo_download / 60)