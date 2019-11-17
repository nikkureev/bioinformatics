def search(in_list, a):
    counter = 0
    for i in in_list:
        if i == a:
            print(counter)
            break
        counter += 1
