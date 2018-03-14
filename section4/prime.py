prime = int(input('Enter a number: '))

is_prime = True
# for i in range(2,prime):
#     if prime % i == 0:
#         is_prime = False
#         break

i = 2
while i <= prime ** 0.5:
    if prime % i ==0:
        is_prime = False
        break
    i +=1
if is_prime:
    print('a prime')
else:
    print('not a prime')
