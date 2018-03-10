
from random import randint
n = randint(0, 100)

count = 0
playing = True
while True:
    a = int(input('Guess my number: '))
    if a < n:
        print('too small')
    elif a > n:
        print('too big')
    else:
        print('Bingo')
        break

    count +=1
    if count == 7:
        print("you lose")
        break
