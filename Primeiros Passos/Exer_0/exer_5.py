"""
Peça ao usuário para digitar números separados por espaço
armazene em uma lista, e imprima a soma apenas dos números pares.
"""

numbers = input('Digite alguns números: ').replace(' ', '')

integers = [int(char) for char in numbers]

print(sum(num for num in integers if num % 2 == 0))

