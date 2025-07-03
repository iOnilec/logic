"""
Operadores
"""

# Adição!
ad = 1 + 1

print(ad)

# Subtração!
sub = 1 - 1

print(sub)

# Multiplicação!
mult = 1 * 1

print(mult)

# Divisão!
div = 1 / 1

print(div)

# Potenciação!
pot = 1 ** 1

print(pot)

# Divisão inteira!
div_in = 1 // 1

print(div_in)

# Resto da divisão!
div_rs = 1 % 1

print(div_rs)

# Ordem de procedência
orddp = (1 + 1) / 1

print(orddp)

# Antes e Depois
num = 5

before = num - 1

after = num + 1

print(f'Antecessor {before} e Sucessor {after}')

# Dobro, Triplo, Raiz
num_x = int(input('Digite um número: '))

print(f'Dobro {num_x * 2}')

print(f'Triplo {num_x * 3}')

print(f'Raiz {num_x ** 0.5}')

# Média
score_n1 = int(input("Digite a primeira nota do Echo: "))

score_n2 = int(input("Digite a segunda nota do Echo: "))

media = (score_n1 + score_n2) / 2 # Ordem de procedência

print(f'A média do Echo é: {media}')

# Métros -> Centímetros -> Milímetros
meters = float(input("Digite os métros: "))

cm = meters * 100
mm = meters * 1000

print(f'Centímetros: {cm}')
print(f'Milímetros: {mm}')