#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for i in range(5):
    peso = float(input(f'Digite o peso da {i+1}ª pessoa (em kg): '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        maior = max(maior, peso)
        menor = min(menor, peso)
print(f'O maior peso lido foi {maior} kg.')
print(f'O menor peso lido foi {menor} kg.')