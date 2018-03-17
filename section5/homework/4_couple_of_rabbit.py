
list_of_couple = ['bome']

print('Month 0: 1 pair of rabbit')

for j in range(4):
    for i in range(len(list_of_couple)):
        if list_of_couple[i] == 'bome':
            list_of_couple.append('haicon')
        if list_of_couple[i] == 'haicon':
            list_of_couple[i] = 'bome'
    print('Month {}: {} pairs of rabbit'.format(j+1,len(list_of_couple)))
