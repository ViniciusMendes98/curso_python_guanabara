#Melhore o ex061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 0
total = 10
while cont < total:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
    if cont == total:
        print('FIM')
        mais = int(input('Deseja mostrar mais quantos termos? '))
        total += mais
print(f'Progresso finalizada com {total} termos mostrados.')