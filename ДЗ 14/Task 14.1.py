import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('C:/Theileria_seq/train.csv', delimiter=',')
df = pd.DataFrame(data.iloc[:, 6:10])
my_first_hist = df.hist()
plt.show()
