from Bio import SeqIO

path_in, path_out, min_len = str(input())
seqs = []
for record in SeqIO.parse(path_in, "fastq"):
    if len(record.seq) > min_len:
        seqs.append(record)
SeqIO.write(seqs, path_out, 'fasta')
