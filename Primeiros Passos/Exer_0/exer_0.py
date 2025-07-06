"""
Crie uma lista chamado notas com 5 notas de um aluno.

- Calcule a média das notas
- Imprima quais notas são maiores que a média
"""

notes = [6, 7, 9, 10, 6]

#notes_sum = sum(notes)
#print(notes_sum)

media = sum(notes) / 5

for note in notes:
    
    if media < note:
        print(note)