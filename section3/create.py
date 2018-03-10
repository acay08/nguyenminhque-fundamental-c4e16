
menu = ['a','b','f']

print(len(menu))

print(menu[0])   # lay ra phan tu so 0



print(*menu, sep=', ')
n = input('add one more:')

menu.append(n)
print(*menu, sep=', ')
