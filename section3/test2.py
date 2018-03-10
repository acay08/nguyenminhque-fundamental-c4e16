from random import choice

n = list('champion')

random_word = choice(n)
len_of_champion = len(n)

new_word = []
new_word.append(random_word)
len_of_new_word = len(new_word)

playing = True
while True:
    random_word = choice(n)
    for i in range(len_of_new_word):
        while random_word == new_word[i]:
            break
    new_word.append(random_word)
    if len_of_new_word == len_of_champion:
        break
print(new_word)
