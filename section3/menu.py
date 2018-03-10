
menu = ['rau muống','cá viên chiên','phở','sườn xào chua ngọt','rau']

# for i in range(len(menu)):
#     print(i+1,'. ', menu[i],sep='')
#
for index, item in enumerate(menu):
    print(index+1,'. ',item, sep='')

# for item in menu:
#     print(item)

menu[0] = 'rau má'

print(*menu, sep=', ')
