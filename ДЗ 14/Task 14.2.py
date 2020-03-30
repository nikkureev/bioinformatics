import pandas as pd


data = pd.read_csv('C:/Theileria_seq/train.csv', delimiter=',')
df = data[data['matches'] > data['matches'].mean()]
df = df[['reads_all', 'mismatches', 'deletions', 'insertions']]
print(df)
