import numpy
import random
import matplotlib.pyplot as plt

n = 10000

x = numpy.zeros(n)
y = numpy.zeros(n)

for i in range(1, n):
    j = random.randint(1, 4)
    if j == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif j == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif j == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

plt.plot(x, y)
plt.show()
