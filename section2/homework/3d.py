print('10 x 10 1’s and 0’s:')

for i in range(10):
    if i % 2 == 0:
        print('1 0 ' * 10,end='')
    else:
        print('0 1 ' * 10,end='')
    print()


n = int(input('Enter a number: '))

for i in range(n):
    if i % 2 == 0:
        print('1 0 ' * n, end='')
    else:
        print('0 1 ' * n, end='')
    print()
