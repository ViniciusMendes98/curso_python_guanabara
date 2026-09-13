#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um número para calcular o seu fatorial: '))
cont = n
fatorial = 1
while cont > 0:
    fatorial *= cont
    cont -= 1
print(f'O fatorial de {n} é {fatorial}.')
