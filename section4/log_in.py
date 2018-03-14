print('Hi there, this is a superuser gateway')

count = 0
while True:

    user = input('Username: ')

    if user != 'c4e':
        print('It is not superuser')
    else:
        password = input('Password: ')
        if password != "12345":
            print('incorrect')
        else:
            print('Welcome,c4e')
            break
    count +=1
    if count == 3:
        print('You failed to log in 3 times')
        break
