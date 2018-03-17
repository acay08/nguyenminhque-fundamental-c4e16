import string

string1 = input('Enter a string: ')
list_of_str = list(string1)

alpha = list(string.ascii_lowercase)

data = {}

for i in alpha:
    if i in list_of_str:
        j = list_of_str.count(i)
        data[i] = j

for k in data:
    print(k, data[k])
