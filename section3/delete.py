menu = ['rau muống','cá viên chiên','phở','sườn xào chua ngọt','rau']

for index, item in enumerate(menu):
    print(index+1,'. ',item, sep='')

print('*' * 20)

n = int(input('Position wants delete? '))
del menu[n-1]   #remove  #del  #pop

print('*' * 20)

for index, item in enumerate(menu):
    print(index+1,'. ',item, sep='')

# menu.pop(n-1)
# print('*' * 20)
#
# for index, item in enumerate(menu):
#     print(index+1,'. ',item, sep='')
