
item = ['T-Shirt', 'Sweater']

conti = 'yes'
while conti == 'yes':

    action = input('Welcome to our shop, what do you want (C, R, U, D): ')

    if action not in ['C','R','U','D']:
        print('wrong character, please try again!')
    else:
        while action in ['C','R','U','D']:
            if action =='R':
                print('Our items: ', end='')
                print(*item, sep=', ')
                break
            elif action =='C':
                new = input('Enter new item: ')
                item.append(new)
                print('Our items: ', end='')
                print(*item, sep=', ')
                break
            elif action == 'U':
                pos = int(input('Update position: '))
                while pos > len(item):
                    print('out of range, pls choose a number smaller or equal ', len(item))
                    pos = int(input('try again, Update position: '))
                new = input('New item? ')
                item[pos-1] = new
                print('Our items: ', end='')
                print(*item, sep=', ')
                break
            else:
                dele = int(input('Delete position? '))
                while dele > len(item):
                    print('out of range, pls choose a number smaller or equal ', len(item))
                    dele = int(input('try again, Delete position: '))
                del item[dele-1]
                print('Our items: ', end='')
                print(*item, sep=', ')
                break
    conti = input('continue, input yes or no: ')
