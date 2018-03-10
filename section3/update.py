

menu = ['rau muống','cá viên chiên','phở','sườn xào chua ngọt','rau']

for index, item in enumerate(menu):
    print(index+1,'. ',item, sep='')

print('*' * 20)
n = int(input('Position wants updated? '))
monmoi = input('New one?: ')

print('*' * 20)

menu[n-1] = monmoi
for index, item in enumerate(menu):
    print(index+1,'. ',item, sep='')
