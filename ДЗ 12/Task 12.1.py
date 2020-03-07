first_list = [1, 2, 3, 4, 5, 6, 7]
second_list = list(map(lambda x: x + 1, first_list))
print(second_list)
 
third_list = list(map(lambda x,y: x + y, first_list, second_list))
print (third_list)

fourth_list = list(map(str, first_list))

ff_list = list(filter(lambda x: x > 4, first_list))

sf_list = list(filter(lambda x, y: + y, first_list, second_list))


