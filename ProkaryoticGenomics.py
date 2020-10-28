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
