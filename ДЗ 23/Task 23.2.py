import matplotlib.pyplot as plt
import numpy as np


plt.axis('off')
path = '/home/nikolay/cute.png'
img = plt.imread(path, 0)
plt.imshow(img)

kernel = [[-1, 2, -1],
          [2, -1, 2],
          [-1, 2, -1]]

modified = np.zeros_like(img)

for row in range(1, img.shape[0] - 2):
    for col in range(1, img.shape[1] - 2):
        modified[row, col] = (img[row: row + 3, col: col + 3] * kernel).sum()

plt.imshow(modified, cmap='gray')
plt.savefig('/home/nikolay/crop.png')
