inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}

for k in inventory:
    print(k,': ', inventory[k])

print('*' * 50)
print("after adding 'pocket', we have: ")
inventory["pocket"] = ['seashell', 'strange berry', 'lint']
for k in inventory:
    print(k,': ', inventory[k])

print('*' * 50)
print("after removing 'dagger' out of 'backpack', we have: ")
inventory['backpack'].remove('dagger')
for k in inventory:
    print(k,': ', inventory[k])

print('*' * 50)
print("after adding 50 to the number stored under the 'gold' key: ")
inventory['gold'] += 50
for k in inventory:
    print(k,': ', inventory[k])
