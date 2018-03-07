print()
print('Factorial of a number')
a = int(input('Number = '))

total = 1
for i in range(1,a+1):
    total = total * i
print('Factorial = ',total)
