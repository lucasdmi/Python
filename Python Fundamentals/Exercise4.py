#Escreva um programa que lê um número inteiro e imprime o seu fatorial.



def fatorial(numero):

    if(numero == 0):
        return 1
    else:
        fatorial = 1
        for i in range(0, numero):
            fatorial = (numero - i) * fatorial
    return fatorial


numero = int(input("Digite um número inteiro: "))
fatorial = fatorial(numero)
print(f"O fatorial do numero {numero} é {fatorial}")
