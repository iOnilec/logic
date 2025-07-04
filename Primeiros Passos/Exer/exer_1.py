"""
Crie um dicionário aluno com as chaves:

- nome (str)
- idade (int)
- notas (lista de 4 notas)
"""

students = [
    {
        'name': 'Igor Ximenes',
        'age': 20,
        'notes': [7, 8, 7, 10],
    },
    {
        'name': 'Jackson Demésio',
        'age': 21,
        'notes': [8, 9, 4, 5,]
    },
    {
        'name': 'Cesar Augusto',
        'age': 21,
        'notes': [5, 5, 6, 7,]
    },
]

for student in students:
    print(student['name'], sum(student['notes']) / 4)

    if sum(student['notes']) / 4 >= 7:
        print('Aprovado!')
    else:
        print('Reprovado!')