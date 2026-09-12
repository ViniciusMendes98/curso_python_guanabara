#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
if frase == frase[::-1]:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
