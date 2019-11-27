from Bio.Seq import Seq

start = ['ATG']
stop = ['TAG', 'TAA', 'TGA']
sequence_for = Seq(input())
sequence_rev = sequence_for.reverse_complement()

for_starts, rev_starts, for_stops, rev_stops = [], [], [], []
for nucs in range(len(sequence_for) - 2):
    if str(sequence_for[nucs] + sequence_for[nucs + 1] + sequence_for[nucs + 2]) in start:
        for_starts.append(nucs)
    elif str(sequence_for[nucs] + sequence_for[nucs + 1] + sequence_for[nucs + 2]) in stop:
        for_stops.append(nucs)
    elif str(sequence_rev[nucs] + sequence_rev[nucs + 1] + sequence_rev[nucs + 2]) in start:
        rev_starts.append(nucs)
    elif str(sequence_rev[nucs] + sequence_rev[nucs + 1] + sequence_rev[nucs + 2]) in stop:
        rev_stops.append(nucs)

for_genes, rev_genes = [], []
for i in for_starts:
    for j in for_stops:
        if j - i >= 9 and (j - i) % 3 == 0:
            for_genes.append(sequence_for[i:j + 3])

for i in rev_starts:
    for j in rev_stops:
        if j - i >= 9 and (j - i) % 3 == 0:
            rev_genes.append(sequence_rev[i:j + 3])
