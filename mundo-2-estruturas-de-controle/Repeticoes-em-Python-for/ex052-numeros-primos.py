#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número inteiro: '))
divisores = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1
if divisores == 2:
    print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo.')