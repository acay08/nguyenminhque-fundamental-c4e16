prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
}

for k in prices:
    print(k.upper())
    print('price: ', prices[k])
    print('stock: ', stock[k])
    print()

total = 0

for k in prices:
    total_k = prices[k] * stock[k]
    print("total money for {} is {}".format(k, total_k))
    total += total_k

print()
print('Total money if all food was sold would be: ',total)
