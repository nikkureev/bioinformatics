import numpy as np
import time
import matplotlib.pyplot as plt


def sort_check(in_list, sort_direct_min_max=True):  # you can check sorted status in two directions
    for i in range(len(in_list) - 1):
        if sort_direct_min_max:
            if in_list[i] > in_list[i + 1]:
                return False
        else:
            if in_list[i] < in_list[i + 1]:
                return False
    return True


def monkey_sort(min_n, max_n, length_of_list):
    a = np.random.randint(min_n, max_n, length_of_list)
    start = time.time()
    while not(sort_check(a)):
        np.random.shuffle(a)
    end = time.time()
    xy = end - start
    return xy


l, x, y = [], [], []
for i in range(10):
    k = []
    for j in range(10):
        k.append(monkey_sort(0, 3, i))
    l.append(k)
for i in range(len(l)):
    x.append(i)
    y.append(np.average(l[i]))
    plt.text(i, np.average(l[i]) - 0.0025, str(round(np.average(l[i]), 4)) + '+-' + str(round(np.var(l[i]), 4)))
f = plt.plot(x, y)
plt.show()
