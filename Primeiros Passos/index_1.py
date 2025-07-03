"""
Tipos primitivos e saida de dados
"""

# int()
n1 = int(input('Número 1: '))

n2 = int(input('Número 2: '))

print(n1 + n2)

# float()
n1_fl = float(input('Número 1.1: '))

n2_fl = float(input('Número 2.2: '))

print(n1_fl + n2_fl)

print('Float: {}'.format(n1_fl + n2_fl))

print('Float:', n1_fl + n2_fl)

print(f'Float: {n1_fl + n2_fl}') # Algumas saídas de dados diferentes

# isObject()
thing = input("Digite algo: ")

print(f"""
    - O tipo primitivo desse valor é {type(thing)}
    - Só tem espaços? {thing.isspace()}
    - É um número? {thing.isnumeric()}
    - É um alfabético? {thing.isalpha()}
    - É um alfanúmerico? {thing.isalnum()}
    - Esta em maiúscula? {thing.isupper()}
    - Esta em minúscula? {thing.islower()}
    - Esta captalizada? {thing.istitle()}
""")