print('CODE')
sz = int(input('Enter size of the letter CODE: '))
if sz%2 ==0:
    sz = sz + 1
else:
    print()

a = 1
for i in range(sz):
    if a == 1 or a == sz:
        print('  ','x '* (sz-1), '  ' * 2, end='')
        print('  ','x '* (sz-2), '  ', '  ' * 2, end='')
        print('x '* (sz-1), '  ', '  ' * 2, end='')
        print('x '* (sz), '  ' * 2, end='')
        print()
    elif a != (float(sz/2) + 0.5):
        print('x ','  '*(sz-1), '  ' * 2, end='')
        print('x ','  '*(sz-2),'x ', '  ' *2, end='')
        print('x ','  '*(sz-2),'x ', '  ' *2, end='')
        print('x ','  '*(sz-1), '  ' * 2, end='')
        print()
    else:
        print('x ','  '*(sz-1), '  ' * 2, end='')
        print('x ','  '*(sz-2),'x ', '  ' *2, end='')
        print('x ','  '*(sz-2),'x ', '  ' *2, end='')
        print('x '* (sz-2), '  ' * 2, end='')
        print()
    a +=1
