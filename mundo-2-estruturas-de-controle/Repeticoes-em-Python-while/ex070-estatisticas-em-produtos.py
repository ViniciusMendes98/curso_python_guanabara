#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato.
total = 0
mais_1000 = 0
mais_barato = 0
nome_mais_barato = ''
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        mais_1000 += 1
    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome
    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break
print(f'\nTotal gasto: R${total:.2f}')
print(f'Produtos acima de R$1000: {mais_1000}')
print(f'O produto mais barato foi {nome_mais_barato}')