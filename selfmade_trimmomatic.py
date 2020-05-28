from Bio import SeqIO
from Bio.SeqUtils import GC
import argparse


parser = argparse.ArgumentParser(description='Trimmomatic')
parser.add_argument('-inf', '--input_forward_reads', help='Input file in fasta format')
parser.add_argument('-inr', '--input_reverse_reads', help='Input file in fasta format')
parser.add_argument('-out', '--output', help='Output file')
parser.add_argument('-d', '--head', help='Removing nuclotides from the head of a read sequence')
parser.add_argument('-t', '--tail', help='Removing nuclotides from the tail of a read sequence')
parser.add_argument('-gc', '--GC_content', help='Optional value of GC-content parameter')
parser.add_argument('-mil', '--minimum_length', help='Optional value of minimum read length')
parser.add_argument('-mal', '--maximum_length', help='Optional value of maximum read length')
parser.add_argument('-number', '--number_of_output_reads', help='Optional value of amount of reads in output files')
parser.add_argument('-miq', '--minimum_quality', help='Optional value of minimum read quality')
parser.add_argument('-maq', '--maximum_quality', help='Optional value of maximum read quality')
parser.add_argument('-nf', 'number_of_files', help='Optional amount of output files')

args = parser.parse_args()

input_forward_reads = args.input_forward_reads
input_reverse_reads = args.input_reverse_reads
output = args.output
head = args.head
tail = args.tail
GC_content = args.GC_content
minimum_length = args.minimum_length
maximum_length = args.maximum_length
number_of_output_reads = args.number_of_output_reads
minimum_quality = args.minimum_quality
maximum_quality = args.maximum_quality
number_of_files = args.number_of_files


def reads_comparer(input_for_list, input_rev_list, number, min_length, max_length, min_quality, max_quality,
                   min_gc_content, max_gc_content, file, head, tail):

    if min_length <= len(input_for_list[number].seq) == len(input_rev_list[number].seq) < max_length:

        if min_quality <= sum(input_for_list[number].letter_annotations["phred_quality"]) \
                / len(input_for_list[number].letter_annotations["phred_quality"]) < max_quality and \
                min_quality <= sum(input_rev_list[number].letter_annotations["phred_quality"]) \
                / len(input_rev_list[number].letter_annotations["phred_quality"]) < max_quality:

            if min_gc_content <= GC(input_for_list[number].seq) < max_gc_content and \
                    min_gc_content <= GC(input_rev_list[number].seq) < max_gc_content:

                string = input_for_list[number].seq
                file.write('>' + str(number) + 'f' + '\n' + str(string.seq[head: len(string) - tail]) + '\n')
                file.write('>' + str(number) + 'r' + '\n' + str(string.seq[head: len(string) - tail]) + '\n')
    return 1


def trimming(path1, path2, output, number_of_reads, head=0, tail=0, min_gc_content=0, max_gc_content=100,
                 min_length=0, max_length=1000, min_quality=0, max_quality=100, number_of_files=1):

    for_list = list(SeqIO.parse(path1, 'fastq'))
    print('first list parsed')
    rev_list = list(SeqIO.parse(path2, 'fastq'))
    print('second list parsed')
    max_i, j = 0, 0
    for j in range(number_of_files):
        print('Opening file...')
        way = str(output + '_%s' + '.fasta') % str(j + 1)
        f = open(way, 'w')
        m = 0
        for i in range(max_i, len(for_list)):
            if m < number_of_reads:
                m += reads_comparer(for_list, rev_list, i, min_length, max_length, min_quality, max_quality,
                                    min_gc_content, max_gc_content, f, head, tail)
            else:
                f.close()
                print('File closed')
                max_i = i
                break


if __name__ == '__main__':

    trimming(input_forward_reads, input_reverse_reads, output,
             head, tail,
             GC_content,
             minimum_length, maximum_length,
             number_of_output_reads,
             minimum_quality, maximum_quality,
             number_of_files)
