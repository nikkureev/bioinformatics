my_first_set = set()
my_second_set = {1, 2, (3, 4, 5)}
my_first_set.add('October')
my_first_set.add(2.0)
t1 = my_first_set.union(my_first_set, my_second_set)
t2 = my_first_set.intersection(my_second_set)
t3 = my_first_set.difference(my_second_set)
t4 = my_first_set.symmetric_difference(my_second_set)
check = my_second_set <= my_first_set
