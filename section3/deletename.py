menu = ['rau muống','cá viên chiên','phở','sườn xào chua ngọt','rau']

for index, item in enumerate(menu):
    print(index+1,'. ',item, sep='')

print('*' * 20)

n = input('what meal do you want to delete? ')

if n in menu:
    menu.remove(n)
else:
    print('not found')


print('*' * 20)

for index, item in enumerate(menu):
    print(index+1,'. ',item, sep='')
