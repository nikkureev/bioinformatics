a_set = {}
a_set['first'] = 1
a_set['second'] = 2
a_set['third'] = 3
a_set[4] = 'fourth'

del a_set['third']
del a_set[4]

print(a_set['first'])
print(a_set['second'])

a_set['new_one'] = a_set['first'] + a_set['second']

