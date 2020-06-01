import pandas as pd
import os


names = []
for files in os.listdir('C:/NGS/Data/'):
    if files.endswith('.tsv'):
        names.append(files.split('.')[0])

data = {}
for i in names:
    with open('C:/NGS/Data/' + i + '.tsv', 'r') as f:
        genes = []
        numbers = []
        for lines in f:
            numbers.append(lines.split()[2])
            genes.append('(' + lines.split()[0] + ')')
        numbers.pop(0)
        genes.pop(0)
        data[i] = numbers

df = pd.DataFrame(data=data)
df.index = genes
df.to_csv('C:/NGS/Data/final.tsv', sep='\t')
