import matplotlib.pyplot as plt
from scipy.stats import norm
from Bio import SeqIO
import numpy as np


def seq_distr(path, sd, smooth=False): # smooth will make yours plot smoothier, appending more values by numpy
    lengths = []
    for seq_record in SeqIO.parse(path, 'fasta'):
        lengths.append(len(seq_record.seq))
    lengths.sort()
    if smooth:
        l_sm = np.array(lengths)
        lengths = np.linspace(l_sm.min(), l_sm.max(), 50)
    plt.plot(lengths, norm.pdf(lengths, sum(lengths) / len(lengths), sd))
    plt.show()


seq_distr('C:/Theileria/just_seq.fasta', 1, smooth=True)
