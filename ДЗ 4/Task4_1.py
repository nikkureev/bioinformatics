def open_list(input_list):
    opened_list = []
    for i in input_list:
        if type(i) == list:
            sup_list = open_list(i)
            for j in sup_list:
                opened_list.append(j)
        else:
            opened_list.append(i)
    return opened_list
