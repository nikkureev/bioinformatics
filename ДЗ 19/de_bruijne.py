from collections import defaultdict, Counter
import copy


def fastaParser(infile):
    seqs = []
    with open(infile, 'r') as f:
        sequence = ""
        header = None
        for line in f:
            if line.startswith('>'):
                if header:
                    seqs.append(sequence)
                sequence = ""
                header = line[1:]
            else:
                sequence += line.rstrip()
        seqs.append(sequence)
    return seqs


def de_bruijn(input_reads, k):
    kmers_counter = defaultdict(Counter)
    for read in input_reads:
        kmers = [read[i: i + k] for i in range(len(read) - k + 1)]
        for i in range(len(kmers) - 1):
            prev_kmer = kmers[i]
            next_kmer = kmers[i + 1]
            kmers_counter[prev_kmer].update([next_kmer])

    graph = {i: {v for v in kmers_counter[i]} for i in kmers_counter}

    out_kmers = defaultdict(int)
    for i in kmers_counter:
        for k in kmers_counter[i]:
            out_kmers[i] += kmers_counter[i][k]

    in_kmers = defaultdict(int)
    for v in kmers_counter.values():
        for kmer in v:
            in_kmers[kmer] += v[kmer]

    return graph, in_kmers, out_kmers


def assembler(de_bruijn, in_kmers, out_kmers):
    assembled_strings = []
    n = 0
    while True:
        refer = copy.deepcopy(de_bruijn)
        n_values = sum([len(refer[k]) for k in refer])
        if n_values == 0:
            break

        best_starts = [k for k in refer if refer[k] and out_kmers[k] > in_kmers[k]]
        if len(best_starts) == 0:
            best_starts = [k for k in refer if refer[k]]
        try:
            current_point = best_starts[n]
        except IndexError:
            break

        assembled_string = current_point
        while True:
            try:
                next_kmer = refer[current_point]
                next_edge = next_kmer.pop()
                assembled_string += next_edge[-1]
                refer[current_point] = next_kmer
                current_point = next_edge
            except KeyError:
                assembled_strings.append(assembled_string)
                n += 1
                break
    return assembled_strings


if __name__ == "__main__":
    ref_file = 'C:/Theileria_seq/test_reads.txt'
    reads = fastaParser(ref_file)
    db_graph, in_degrees, out_degrees = de_bruijn(reads, 3)
    output = assembler(db_graph, in_degrees, out_degrees)
    longest = ''
    for vars in output:
        if len(vars) > len(longest):
            longest = vars
    print(longest)
