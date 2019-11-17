def moda(l):
    all_dict = {}
    for i in l:
        if all_dict.get(i) == None:
            all_dict[i] = 1
        else:
            all_dict[i] += 1

    max_moda = 0
    for i in all_dict.keys():
        if all_dict[i] > max_moda:
            max_moda = all_dict[i]

    new_list = []
    for i in all_dict.keys():
        if all_dict[i] == max_moda:
            new_list.append(i)

    return new_list
