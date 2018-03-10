food1 = 'cá'
food2 = 'phở'
food3 = 'sườn xào chua ngọt'
food4 = 'rau'

menu = ['rau muống','cá viên chiên','phở','sườn xào chua ngọt','rau']


print(*menu, sep=', ')   #pythonic  # sep: separator

menu.append('bún chả')

print(*menu, sep=', ')  
