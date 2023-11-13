#Escreva um programa que lê dois números e imprime a soma, a subtração, a multiplicação e a divisão entre eles.


numero = []
soma = 0

for i in range(0, 2, 1):
    insert = int(input(f'Insira dois números. Numero {i +1}:'))
    numero.append(insert)

soma = numero[0] + numero[1]
divisao = numero[0] / numero [1]
multiplicacao = numero[0] * numero[1]
subtracao = numero[0] - numero[1]

print(f'A soma dos números é: {soma}')
print(f'A divisao dos números é: {divisao}')
print(f'A multiplicacao dos números é: {multiplicacao}')
print(f'A subtracao dos números é: {subtracao}')



