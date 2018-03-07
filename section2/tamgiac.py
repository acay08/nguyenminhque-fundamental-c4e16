a = int(input('canh a:'))

for i in range(a):
    for j in range(i+1):
        print('x ', end="")
    print()
for i in range(a):
    for j in range (a):
        if j >= (a-1-i):
            print('* ',end="")
        else:
            print("  ",end="")
    print()
