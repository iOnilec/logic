"""
Crie uma função is_palindrome(text) que recebe uma string e verifica se ela é um palíndromo 
(desconsiderando espaços e capitalização).
"""

# Entendendo o replace
text = input('digite algo: ')

replace = text.replace('Noite', 'Tarde')

print(replace)

def is_palindrome(text):

    palindrome = text.replace(" ", " ").lower()

    return palindrome == palindrome[::-1]


print(is_palindrome('natan'))

    

