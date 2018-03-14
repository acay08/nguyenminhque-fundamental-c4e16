print('guess your number game')
input('now think a number from 0-100, then press Enter')
print("""
All you have to answer to my game:
'c' if my guess is incorrect
'l' if my guess is larger
's' if my guess is smaller
""")
low = 0
high = 101
while True:
    mid = (low + high) // 2

    ans = input("Is {0} your number? ".format(mid)).lower()

    if ans == "c":
        print('I knew it')
        break
    elif ans == "l":
        high = mid
    elif ans == 's':
        low = mid
    else:
        print('ezzz')
