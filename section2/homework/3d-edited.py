print('10 x 10 1’s and 0’s:')

for i in range(10):
    if i % 2 == 0:
        print('1 0 ' * 5,end='')
    else:
        print('0 1 ' * 5,end='')
    print()


n = int(input('Enter a number: '))
if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            print('1  0  ' * int(n/2), end='')
        else:
            print('0  1  ' * int(n/2), end='')
        print()
else:
    for i in range(n):
        if i % 2 == 0:
            print('1 0 ' * int(n/2), end='')
            print('1')
        else:
            print('0 1 ' * int(n/2), end='')
            print('0')
