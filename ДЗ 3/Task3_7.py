s = 'agatacaca'

s_rev_1 = reversed_string = s[::-1]

s_rev_2 = ''.join(reversed(s))

lett_list = []
for lett in s:
	lett_list.append(lett)
lett_list.reverse()

s_rev_3 = ''
for i in lett_list:
	s_rev_3 += i
