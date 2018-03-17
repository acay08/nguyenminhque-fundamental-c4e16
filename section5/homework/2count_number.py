numbers = [1, 3, 5, 7, 8, 1, 5, 1]

print('numbers =',numbers)

k = int(input('Enter a number: '))

times = 0

for i in numbers:
    if i == k:
        times +=1

print('{} appears {} times in my list'.format(k,times))
