
flock = [5,7,300,90,24,50,75]
print('Hello, my name is Acay and these are my sheep sizes:')
print(flock)

print()
biggest = max(list(flock))
print('Now my biggest sheep has size ',biggest ,"let's sheer it")

print()
index_of_biggest = flock.index(biggest)
flock[index_of_biggest] = 8
print('After shearing, here is my flock:')
print(flock)

print()
numbers_of_sheeps = len(flock)
for i in range(numbers_of_sheeps):
    flock[i] += 50
print('One month has passed, now here is my flock:')
print(flock)
