from Bio import SeqIO


def select(path_in, path_out, min_len=50):
    seq = []
    for record in SeqIO.parse(path_in, "fastq"):
        if len(record.seq) > min_len:
            seq.append(record)
    SeqIO.write(seq, path_out, 'fasta')
