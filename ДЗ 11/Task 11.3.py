a = [1, 2, 3, 4, 5]


def sort_check(in_list, sort_direct_min_max=True): # you can check soted status in two directions
    for i in range(len(in_list) - 1):
        if sort_direct_min_max:
            if in_list[i] > in_list[i + 1]:
                print('Not sorted')
                return
        else:
            if in_list[i] < in_list[i + 1]:
                print('Not sorted')
                return
    print('Sorted')


sort_check(a)
