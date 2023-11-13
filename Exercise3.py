#Escreva um número que imprima os números primos de 1 a 100.


def eh_primo(numero):
    for i in range (2, numero):
        if numero % i == 0:
            return False
    return True

for i in range(2,101):
    if eh_primo(i):
        print(i)