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
        for h in hs:
            read_out.append([h.hit_id, h.bitscore, h.hit_range])
    result[hsp.id] = read_out

for i, v in result.items():
    if len(v) == 2:
        if v[1][2][0] == 1:
            v.append(1)
        else:
            v.append(len(result))
    else:
        

for i, v in result.items():
    print(i, v)
