a_list = ['one', 'one', 'two', 'three']
a_set = set(a_list)
a_tuple = tuple(a_list)
a_str = ''
for i in a_list:
	a_str += i

a_tuple_2 = ('one', 'one', 'two', 'three')
a_str_2 = ''.join(a_tuple_2)
a_list_2 = list(a_tuple_2)
a_set_2 = set(a_tuple_2)

a_set_3 = {'one', 'two', 'three'}
a_str_3 = ''.join(a_set_3)
a_list_3 = list(a_set_3)
a_tuple_3 = tuple(a_set_3)

a_str_4 = 'one_one_two_three'
a_list_4 = [i for i in a_str_4.split('_')]
a_tuple_4 = (i for i in a_str_4.split('_'))
a_set_4 = {i for i in a_str_4.split('_')}

