import os


source = 'C:/AGlab/IB/ncbi-genomes-2020-10-21/opened/'
final = 'C:/AGlab/gene_rRNA.txt'

g = open(final, 'w')
g.close()

files = os.listdir(source)
for gff in files:
    with open(source + gff, 'r') as f:
        string = ''
        #string += gff.split('.')[0] + ' '
        for lines in f:
            if not lines.startswith('#'):
                if lines.split()[2] == 'rrna':
                    string += lines.split()[8].split(';')[0].split('-')[1].split('_')[1] + ' '
        string += '\n'
        g = open(final, 'a')
        g.write(string)
        g.close()
        
        
        
#####################################################        
import matplotlib.pyplot as plt


file = 'C:/AGlab/gene_sorted.txt'
table = 'C:/AGlab/gene_table.txt'
gene_dict = {}

with open(file, 'r') as f:
    for lines in f:
        for gene in lines.split():
            if gene in gene_dict.keys():
                gene_dict[gene] += 1
            else:
                gene_dict[gene] = 1

numb_dict = {}
for val in gene_dict.values():
    if val in numb_dict.keys():
        numb_dict[val] += 1
    else:
        numb_dict[val] = 1

for i, v in gene_dict.items():
    print(i, v)
# with open(table, 'w') as d:
#     for i, v in numb_dict.items():
#         d.write(str(i) + ' ' + str(v) + '\n') 
