def puzirok(in_list):
    for i in range(len(in_list) - 1):
        for j in range(len(in_list) - i - 1):
            if in_list[j] > in_list[j + 1]:
                in_list[j], in_list[j + 1] = in_list[j + 1], in_list[j]
    return in_list
