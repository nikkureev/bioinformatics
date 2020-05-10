import os
from Bio import SearchIO
from Bio.Blast.Applications import NcbiblastnCommandline


class Read:

    class Subread:

        def __init__(self, read_number, score, h_range, h_seq):
            self.read_number = read_number
            self.score = score
            self.h_range = h_range
            self.h_seq = h_seq

    def __init__(self, ids, length=0, prev_read=0, range_of_prev=0, next_read=0, range_of_next=0):
        self.ids = ids
        self.length = length
        self.prev_read = prev_read
        self.next_read = next_read
        self.range_of_prev = range_of_prev
        self.range_of_next = range_of_next
        self.info = []

    def align_to(self, rn, s, hr, hsc):
        self.rn = rn
        self.s = s
        self.hr = hr
        self.hsc = hsc
        self.info.append(self.Subread(rn, s, hr, hsc))

    def matches(self):
        return self.info


def alignfunc(in_list, out_f):
    in_file = in_list[0]
    db_file = in_list[1]
    cmd = r'/home/nikolay/makeblastdb -in %s -dbtype nucl' % db_file
    os.system(cmd)
    proga = r'/home/nikolay/blastn'
    blast = NcbiblastnCommandline(proga, query=in_file, db=db_file, out=out_f, outfmt=5,
                                  word_size=4)
    stdout, stderr = blast()


def read_maker(input_blast):
    result = []
    for hsp in input_blast:
        sample_read = Read(hsp.id)
        for hs in hsp:
            hit_ids = []
            for h in hs:
                if h.hit_id not in hit_ids:
                    sample_read.align_to(h.hit_id, h.bitscore, h.hit_range, h.query.seq)
                    hit_ids.append(h.hit_id)
        result.append(sample_read)
    return result


def sequence_establishing(input_list):
    for ones in input_list:
        for ks in ones.info:
            if ks.read_number != ones.ids:
                if ks.h_range[0] == 0:
                    ones.next_read = ks.read_number
                    ones.range_of_next = ks.h_range
                else:
                    ones.prev_read = ks.read_number
                    ones.range_of_prev = ks.h_range
            else:
                ones.length = len(ks.h_seq)


def sequence_assembly(result_list):
    assembled_seq = ''
    former, former_range = 0, 0

    for samples in result_list:
        if samples.prev_read == 0:
            for ls in samples.info:
                if ls.read_number == samples.ids:
                    assembled_seq += ls.h_seq
                    former = samples.next_read
                    former_range = samples.range_of_next

    while former:
        for samples in result_list:
            if samples.ids == former:
                for js in samples.info:
                    if js.read_number == former:
                        newens = [former_range[1], samples.length]
                        assembled_seq += js.h_seq[newens[0]:newens[1]]
                        former = samples.next_read
                        former_range = samples.range_of_next

    return assembled_seq


def main(input_file, input_outfile):
    alignfunc([input_file, input_file], input_outfile)

    blast_res = SearchIO.parse(input_outfile, "blast-xml")
    l1 = read_maker(blast_res)
    sequence_establishing(l1)
    l2 = sequence_assembly(l1)

    print('RESULT SEQUENCE: ', l2)


if __name__ == '__main__':
    main('/home/nikolay/simple_reads.txt', '/home/nikolay/align.xml')
