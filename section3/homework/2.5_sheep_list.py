
flock = [5,7,300,90,24,50,75]

print('Hello, my name is Acay and these are my sheep sizes:')
print(flock)

number_of_months = int(input('Enter the number of months: '))
number_of_sheeps = len(flock)
for j in range(number_of_months):
    for i in range(number_of_sheeps):
        flock[i] += 50
    print('MONTH',j+1)
    print('One month has passed, now here is my flock:')
    print(flock)
    biggest = max(list(flock))
    print('Now my biggest sheep has size ',biggest ,"let's sheer it")
    index_of_biggest = flock.index(biggest)
    flock[index_of_biggest] = 8
    print('After shearing, here is my flock:')
    print(flock)
    print()
