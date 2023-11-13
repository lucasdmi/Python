#Escreva um programa que lê um número e imprime a sua tabuada
numero = int(input('Insira um número para calcular a sua tabuada: '))

for i in range(1,11):
    multiplica = numero * i
    print(f'Tabuada de {numero} x {i} é {multiplica}')
     
