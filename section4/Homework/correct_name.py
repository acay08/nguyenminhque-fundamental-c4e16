name = input('Your full name: ')

while '  ' in name:
    name = name.replace('  ',' ')

name = name.lower().strip().title()

print('Updated name:',name)
