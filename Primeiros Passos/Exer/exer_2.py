"""
Crie uma função is_even(num) que retorna True se o número for par e False caso contrário.
Peça para o usuário digitar um número e use a função para informar se ele é par ou ímpar.
"""

def is_even(num):

    if num % 2 == 0:
        return True
    else:
        
        i = int(input('Digite outro número: '))

        if i % 2 == 0:
            print('Número par')
        else:
            print('Número impar')

            return False

print(is_even(11))

