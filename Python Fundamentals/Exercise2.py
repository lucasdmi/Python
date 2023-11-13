#Escreva um programa que imprima os números pares de 1 a 100.
#Em programação, o resto é o valor que sobra quando um número é dividido por outro. 
#Por exemplo, 10 dividido por 3 é igual a 3, com um resto de 1. O operador de resto, geralmente representado pelo símbolo "%", é usado para calcular o resto de uma divisão.



for i in range(2, 101):
    resto = int(i % 2) 
    if  resto == 0:
        print(f"Numero par: {i}")
    

#opcao 2
for i in range(2, 101, 2): #Começa no numero 2, vai até 100 e o for é executado de 2 em 2. 
        print(f"Numero par - opcao 2: {i}")


