def search(in_list, a):
    in_list.sort()
    low = 0
    high = len(in_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if a < in_list[mid]:
            high = mid - 1
        elif a > in_list[mid]:
            low = mid + 1
        else:
            print("ID =", mid)
            break
    else:
        print("No the number")
