s = str(input())

it = s.istitle()
l = len(s)
ie = s.endswith('!!')
fire = s.count('fire')
up = s.upper()
low = s.lower()

print('start with title? ', it, '\nlength: ', l, '\nend with !!? ', ie, '\nfire count: ', fire, '\n', up, '\n', low, sep='')
