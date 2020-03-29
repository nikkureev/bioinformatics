from Bio import SeqIO
import matplotlib.pyplot as plt
from Bio.SeqUtils import GC
import re
import itertools



def dict_filling(dictionary, stats, sequence):
    for i in range(len(stats)):
        for nucs in stats:
            length = len(re.findall(nucs, str(sequence).upper()))
            if length != 0:
                dictionary[nucs] = length


def four_mers_stats(DNA_four_mers, sequence):
    four_mers_statistic = {}
    dict_filling(four_mers_statistic, DNA_four_mers, sequence)
    return four_mers_statistic


def codon_stats(DNA_codons, sequence):
    codons_statistic = {}
    dict_filling(codons_statistic, DNA_codons, sequence)
    return codons_statistic


def temperature(sequence):
    adenine = sequence.upper().count('A')
    thymine = sequence.upper().count('T')
    cytosine = sequence.upper().count('C')
    guanine = sequence.upper().count('G')
    return ((adenine + thymine) * 2 + (guanine + cytosine) * 4)


def loops_stats(sequence):
    loops = {}
    if len(sequence) > 10:
        for i in range(len(sequence) - 7):
            DNA_loop = sequence[i: i + 3]
            loop_end = sequence[i + 7:].find(DNA_loop.reverse_complement())
            loop = sequence[i + 3: loop_end]
            if len(loop) > 3 and loop_end > 0:
                loops[str(loop)] = [(i, i + 3), (loop_end, loop_end + 3)]
    return loops


class Fastq():

    def __init__(self, path, four_mers_statistics='NA', codons_statistics='NA', tm_annealing='NA', loops='NA', all='NA'):
        self.path = path
        self.record = list(SeqIO.parse(self.path, 'fasta'))
        self.all = all

        if self.all != 'NA':
            four_mers_statistics = '0'
            codons_statistics = '0'
            tm_annealing = '0'
            loops = '0'


        self.four_mers_statistics = four_mers_statistics
        self.codons_statistics = codons_statistics
        self.tm_annealing = tm_annealing
        self.loops = loops

        alphabet = 'ATGC'
        self.DNA_four_mers = []
        self.DNA_codons = []
        for item in itertools.product(alphabet, repeat=4):
            self.DNA_four_mers.append(''.join(item))
        for item in itertools.product(alphabet, repeat=3):
            self.DNA_codons.append(''.join(item))

        class Sequence():

            def __init__(self, description, len, GC_content, four_mers_stats, codons_stats, tm_annealing_stats, loops_stats):
                self.description = description
                self.len = len
                self.GC_content = GC_content
                self.four_mers_statistic = four_mers_stats
                self.codons_statistic = codons_stats
                self.tm_annealing = tm_annealing_stats
                self.loops = loops_stats

        # amount of sequences
        self.amount_of_fastas = len(list(self.record))

        # sequences single statistics
        self.sequence_list = []

        self.len_list = []
        self.gc_content = []

        for self.fastas in self.record:
            self.len_list.append(len(self.fastas.seq))

            # GC_content
            self.gc_content.append(round(GC(self.fastas.seq), 2))

            fm = self.four_mers_statistics
            if self.four_mers_statistics != 'NA':
                fm = four_mers_stats(self.DNA_four_mers, self.fastas.seq)

            cs = self.codons_statistics
            if self.codons_statistics != 'NA':
                cs = codon_stats(self.DNA_codons, self.fastas.seq)

            tm = self.tm_annealing
            if self.tm_annealing != 'NA':
                tm = temperature(self.fastas.seq)

            ls = self.loops
            if self.loops != 'NA':
                ls = loops_stats(self.fastas.seq)


            self.sequence_list.append(Sequence(self.fastas.description,
                                               len(self.fastas.seq),
                                               GC(self.fastas.seq),
                                               fm,
                                               cs,
                                               tm,
                                               ls))


    def file_len(self):
        return self.amount_of_fastas

    def GC_content(self):
        return self.gc_content

    def sequences_lens(self):
        return self.len_list

    def histo(self):
        n_bins = len(self.len_list)
        plt.hist(self.len_list, n_bins)
        plt.show()

    def four_mers(self):
        f_list = []
        for self.fastas in self.record:
            fm = four_mers_stats(self.DNA_four_mers, self.fastas.seq)
            f_list.append(fm)
        return f_list

    def codons_stat(self):
        c_list = []
        for self.fastas in self.record:
            cs = codon_stats(self.DNA_codons, self.fastas.seq)
            c_list.append(cs)
        return c_list

    def temperature_stat(self):
        t_list = []
        for self.fastas in self.record:
            t = temperature(self.fastas.seq)
            t_list.append(t)
        return t_list

    def loops_stat(self):
        l_list = []
        for self.fastas in self.record:
            l = loops_stats(self.fastas.seq)
            l_list.append(l)
        return l_list


    def output(self, out_path):
        with open(out_path, 'w') as f:
            for records in self.sequence_list:
                f.write('sequence description:' + records.description + '\n')
                f.write('sequence_length:     ' + str(records.len) + '\n')
                f.write('GC content           ' + str(records.GC_content) + '\n\n')
                f.write('4-mers statistics' + '\n')
                for i, v in records.four_mers_statistic.items():
                    f.write(i + ' : ' + str(v) + '\n')
                f.write('\n')
                f.write('codons statistics' + '\n')
                for i, v in records.codons_statistic.items():
                    f.write(i + ' : ' + str(v) + '\n')
                f.write('\n')
                f.write('temperature annealing: ' + str(records.tm_annealing) + '\n\n')
                f.write('possible loops       ' + '\n')
                for i, v in records.loops.items():
                    f.write(i + ' : ' + str(v) + '\n')
                f.write('=============' + '\n\n\n')


print(Fastq('C:/Theileria/just.txt', all='0').output('C:/Theileria_seq/test.txt'))
