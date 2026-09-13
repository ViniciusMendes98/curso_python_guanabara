#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
soma = cont = 0
while resp in 'Ss':
    n = int(input('Digite um número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        maior = max(maior, n)
        menor = min(menor, n)
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')    