# Strings em Python 

## Fatiamento

```python
frase = 'Curso em Vídeo Python'

print(frase[0:21:2])  # Do índice 0 até o 21, pulando de 2 em 2
print(frase[:5])     # Do início até o índice 5
print(frase[15:])    # Do índice 15 até o final
print(frase[9::3])   # Do índice 9 até o final, pulando de 3 em 3
```

## Funções para Strings

```python
print(len(frase))              # Mostra o comprimento da string
print(frase.count('a'))        # Conta quantas vezes 'a' aparece
print(frase.count('o', 15, 80)) # Conta 'o' entre os índices 15 e 80
print(frase.find('Python'))    # Mostra onde começa 'Python'
print('Curso' in frase)        # Verifica se 'Curso' existe na frase
```

## Manipulação de Strings

```python
print(frase.replace('Python', 'Android'))  # Substitui 'Python' por 'Android'
print(frase.upper())                       # Converte para maiúsculas
print(frase.lower())                       # Converte para minúsculas
print(frase.capitalize())                  # Primeira letra maiúscula
print(frase.title())                       # Primeira letra de cada palavra maiúscula
```

## Removendo espaços

```python
frase2 = '   Aprenda Python   '

print(frase2.strip())   # Remove espaços dos dois lados
print(frase2.rstrip())  # Remove espaços da direita
print(frase2.lstrip())  # Remove espaços da esquerda
```

## Split e Join

```python
print(frase.split())          # Divide a string onde houver espaços

dividido = frase.split()
print(dividido[2][3])         # Acessa o índice 3 da terceira palavra

print(''.join(frase.split())) # Junta a frase removendo os espaços
```

## Invertendo uma String

```python
print(frase[::-1])            # Escreve a string ao contrário

frase_invertida = frase[::-1]
print(frase_invertida)
```

## Condicional com String

```python
if 'Curso' in frase:
    print('YES')
else:
    print('NO')
```
