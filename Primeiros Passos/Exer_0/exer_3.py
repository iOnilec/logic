"""
Peça para o usuário digitar 5 números e armazene em uma lista.
Depois, usando for, percorra a lista e imprima apenas os números maiores que 10.
"""

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = int(input('Digite o terceiro número: '))
num_4 = int(input('Digite o quarto número: '))
num_5 = int(input('Digite o quinto número: '))

list = [num_1, num_2, num_3, num_4, num_5]

for num in list:
    if num > 10:
        print(num)