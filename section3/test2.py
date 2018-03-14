from random import choice

n = list('champion')

len_of_champion = len(n)

new_word = []
rand_word = choice(n)

new_word.append(rand_word)

while True:
    rand_word = choice(n)
    while rand_word in new_word:
        break
    while rand_word not in new_word:
        new_word.append(rand_word)
        break
    len_of_new_word = len(new_word)
    if len_of_new_word == len_of_champion:
        break
print(new_word)

your_answer = input('your answer: ')
if your_answer == 'champion':
    print('Bingo')
else:
    print(':(')
