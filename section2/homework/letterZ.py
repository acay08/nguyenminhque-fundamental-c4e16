print('Z')
sz = int(input('Enter size of the letter Z: '))

a = 1
for i in range(sz):
    if a == 1 or a == sz:
        print('x ' * sz)
    else:
        print('  ' * (sz-a-1),' x',' ' * a)
    a +=1
