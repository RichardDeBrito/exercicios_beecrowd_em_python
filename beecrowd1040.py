notes = input().split()
n1, n2, n3, n4 = float(notes[0]), float(notes[1]), float(notes[2]), float(notes[3])

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1))/10
print(f'Media: {media:.1f}')
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    exam = float(input())
    print(f'Nota do exame: {exam:.1f}')
    newcalc = (media + exam)/2
    if newcalc >= 5.0:
        print('Aluno aprovado.')
    elif newcalc <= 4.9:
        print('Aluno reprovado.')
    print(f'Media final: {newcalc:.1f}')