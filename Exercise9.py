#Escreva um programa que lê um número e imprime o seu valor absoluto.




def valor_absoluto(numero):
    if numero >= 0:
        valor_absoluto = numero
    else:
        valor_absoluto = numero * (- 1)
    
    return valor_absoluto

numero = int(input('Digite um número: '))
valor_absoluto = valor_absoluto(numero)

print(f'O valor absoluto do numero {numero} é {valor_absoluto}') 