ask = input('Enter a sequent of number, separated by space:')
words = ask.strip().split()  #strip()  cut spaces at start/end of string

numbers = []
for word in words:
    numbers.append(int(word))

is_sorted = True

for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        is_sorted = False
        break
if is_sorted:
    print('sorted')
    print(numbers)
else:
    print('unsorted')

    print('Here is your list sorted')
    new_ds = []
    while True:
        n = min(numbers)
        new_ds.append(n)
        numbers.remove(n)
        if len(numbers) == 0:
            break
    print(*new_ds)
