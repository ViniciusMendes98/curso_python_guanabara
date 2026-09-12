#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for i in range(7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'Quantidade de pessoas maiores de idade: {maiores}')
print(f'Quantidade de pessoas menores de idade: {menores}')