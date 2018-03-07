print('9 x 9 numbers:')
a = 1
for i in range(9):
    for j in range(9):
        if (j+1)*a < 10:
            print((j+1)*a,'  ',end='')
        else:
            print((j+1)*a,' ',end='')
    a +=1
    print()


n = int(input('Enter a number: '))
a = 1
for i in range(n):
    for j in range(n):
        if (j+1)*a < 10:
            print((j+1)*a,'  ',end='')
        else:
            print((j+1)*a,' ',end='')
    a +=1
    print()
