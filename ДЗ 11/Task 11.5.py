import matplotlib.pyplot as plt
import random


def serpinsky_triangle(line_len):
    a = [0, 0]
    b = [line_len / 2, line_len]
    c = [line_len, 0]
    ran_point = [random.randint(0, line_len), random.randint(0, line_len)]
    plt.scatter(a[0], a[1])
    plt.scatter(b[0], b[1])
    plt.scatter(c[0], c[1])
    plt.scatter(ran_point[0], ran_point[1])
    for i in range(2000):
        n = random.randint(1, 3)
        if n == 1:
            ran_point = [abs(a[0] + ran_point[0]) / 2, abs(a[1] + ran_point[1]) / 2]
        elif n == 2:
            ran_point = [abs(b[0] + ran_point[0]) / 2, abs(b[1] + ran_point[1]) / 2]
        elif n == 3:
            ran_point = [abs(c[0] + ran_point[0]) / 2, abs(c[1] + ran_point[1]) / 2]
        plt.scatter(ran_point[0], ran_point[1])
    plt.show()


serpinsky_triangle(5)
