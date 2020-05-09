import os
from Bio import SearchIO
from Bio.Blast.Applications import NcbiblastnCommandline


def alignfunc(in_list, out_f):
    in_file = in_list[0]
    db_file = in_list[1]
    cmd = r'/home/nikolay/makeblastdb -in %s -dbtype nucl' % db_file
    os.system(cmd)
    proga = r'/home/nikolay/blastn'
    blast = NcbiblastnCommandline(proga, query=in_file, db=db_file, out=out_f, outfmt=5,
                                  word_size=4)
    stdout, stderr = blast()


file1 = '/home/nikolay/test_reads.txt'
file2 = '/home/nikolay/test_seq.txt'
outfile = '/home/nikolay/align.xml'
alignfunc([file1, file1], outfile)

blast_result = SearchIO.parse(outfile, "blast-xml")

result = {}
for hsp in blast_result:
    read_out = []
    for hs in hsp:
        hit_ids = []
        for h in hs:
            if h.hit_id not in hit_ids:
                read_out.append([h.hit_id, h.bitscore, h.hit_range, h.query.seq])
                hit_ids.append(h.hit_id)
    result[hsp.id] = read_out

for i, v in result.items():
    v.append([0, 0])
    if len(v) == 3:
        if v[1][2][0] == 0:
            v[2][1] = v[1][0]
        else:
            v[2][0] = v[1][0]
    else:
        for ks in v:
            if ks[0] != i:
                try:
                    if ks[2][0] == 1:
                        v[-1][0] = ks[0]
                    else:
                        v[-1][1] = ks[0]
                except IndexError:
                    continue

assembled_seq = ''
for i, v in result.items():
    if v[-1][0] == 0:
        assembled_seq += v[0][3]
        next = v[-1][1]
        while next:
            for ks, vs in result.items():
                if ks == next:
                    assembled_seq += vs[0][3][-1]
                    next = vs[-1][1]
print('RESULT SEQUENCE: ', assembled_seq)
