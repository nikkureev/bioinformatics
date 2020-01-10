import numpy as np
import time
import random
import matplotlib.pyplot as plt

ys1, ys2 = [], []
num_of_numbers = 1
for i in range(10000):
    start1 = time.time()
    for i in range(num_of_numbers):
        np.random.uniform(0, 1)
    end1 = time.time()
    ys1.append(end1 - start1)
    num_of_numbers += 1

num_of_numbers = 1
for i in range(10000):
    start2 = time.time()
    for i in range(num_of_numbers):
        random.uniform(0, 1)
    end2 = time.time()
    ys2.append(end2 - start2)
    num_of_numbers += 1


xs = list(range(1, 10001))
fig = plt.subplot()
fig1 = plt.scatter(xs, ys1)
fig2 = plt.scatter(xs, ys2)
plt.text(xs[-1], ys1[-1], 'numpy')
plt.text(xs[-1], ys2[-1], 'random')
fig.set_xlabel('Количество значений')
fig.set_ylabel('Время')
plt.show()
