from random import*

chars = list('champion')

shuffle(chars)

print(*chars)

your_answer = input('your answer: ')
if your_answer == 'champion':
    print('Hura')
else:
    print(':(')
