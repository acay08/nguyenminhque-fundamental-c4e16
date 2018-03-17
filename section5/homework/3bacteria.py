bacterias = int(input('How many B bacterias are there?: '))
minutes = int(input('How many time in minutes will we wait? :'))

final_bacterias = bacterias
for i in range(1, int(minutes/2+1)):
    final_bacterias *= 2

print('After {} minutes, we would have {} bacterias'.format(minutes,final_bacterias))
