import os
import sys
import argparse
import logging
from Bio import SeqIO, SearchIO


parser = argparse.ArgumentParser()
parser.add_argument('-in', '--input', help='input fasta file')
parser.add_argument('-ri', '--read_indexing', help='False (default) if reads have distinguishable identifiers')
parser.add_argument('-ids', '--indexing_file', help='saving indexing file (if True) if --read_indexing is True')
parser.add_argument('-contig', '--contig_file', help='saving contig file (if True)')
parser.add_argument('-log', '--logging_file', help='saving log file (if True)')
parser.add_argument('-out', '--output_file', help='output directory')
parser.add_argument('-wd', '--working_directory',
                    help='set working directory (without "/" at the end), if None current directory will be used')
args = parser.parse_args()
input_fasta_file = args.input
output_file = args.output_file
input_error, save_index_file, save_contig_file, save_logging_file = False, False, False, False
working_directory = os.path.abspath(os.curdir)
if args.read_indexing:
    input_error = True
if args.indexing_file:
    save_index_file = True
if args.contig_file:
    save_contig_file = True
if args.logging_file:
    save_logging_file = True
if args.working_directory:
    working_directory = args.working_directory


def alignfunc(db_file, q_file, align_file):
    proga = r'blastn -query %s -out %s -db %s -outfmt 5 -word_size 4' % (q_file, align_file, db_file)
    os.system(proga)


def indexing(source_file, index_file):
    n = 0
    with open(index_file, 'w') as f:
        for seqs in SeqIO.parse(source_file, 'fasta'):
            if 'unknown' in seqs.id:
                seqs.id = 'read' + str(n)
                f.write('>' + str(seqs.id) + '\n' + str(seqs.seq) + '\n')
                n += 1


def contigassambler(input_file, align_file, mid_file, index_file, contigs_file, num, error_description=True):
    n = 0
    contigs_file = contigs_file + str(num)
    f = open(contigs_file, 'w')
    f.close()
    if error_description:
        indexing(input_file, index_file)
    else:
        index_file = input_file
    cmd = r'makeblastdb -in %s -dbtype nucl' % index_file
    os.system(cmd)
    numbers = []
    logging.debug(index_file)
    for seqs in SeqIO.parse(index_file, 'fasta'):
        logging.warning('Starting...')
        if seqs.id not in numbers:
            numbers.append(seqs.id)
            with open(mid_file, 'w') as f:
                f.write('>' + str(seqs.id) + '\n' + str(seqs.seq))
            alignfunc(index_file, mid_file, align_file)
            for records in SearchIO.parse(align_file, 'blast-xml'):
                max_score = 0
                best_hit, best_hit_id = None, None
                for hits in records:
                    if hits.id != seqs.id and hits.id not in numbers:
                        numbers.append(hits.id)
                        for hsp in hits:
                            if max_score < hsp.bitscore:
                                max_score = hsp.bitscore
                                best_hit = hsp
                                best_hit_id = hits.id
                if best_hit and best_hit_id:
                    logging.debug(best_hit)
                    logging.debug(best_hit_id)
                    try:
                        if best_hit.query_range == best_hit.hit_range:
                            ref = best_hit.query.seq
                            with open(contigs_file, 'a') as f:
                                f.write('>contig' + str(n) + '\n' + str(ref) + '\n')
                                n += 1
                        else:
                            logging.debug('Splitting reads')
                            query_seq, hit_seq = '', ''
                            for strs in SeqIO.parse(index_file, 'fasta'):
                                if strs.id == seqs.id:
                                    query_seq = strs.seq
                                elif strs.id == best_hit_id:
                                    hit_seq = strs.seq
                            if best_hit.hit_range[0] == 0:
                                ref = query_seq + hit_seq[best_hit.hit_range[1]:len(hit_seq)]
                                logging.debug(ref)
                                with open(contigs_file, 'a') as f:
                                    f.write('>contig' + str(n) + '\n' + str(ref) + '\n')
                                    n += 1
                            elif best_hit.query_range[0] == 0:
                                ref = hit_seq + query_seq[best_hit.query_range[1]:len(hit_seq)]
                                with open(contigs_file, 'a') as f:
                                    f.write('>contig' + str(n) + '\n' + str(ref) + '\n')
                                    n += 1
                    except AttributeError:
                        break
    if n == 1:
        with open(output_file, 'w') as out:
            out.write('>assembled_sequence' + '\n' + str(ref))
    return contigs_file


def main(input_file, align_file, mid_file, index_file, contigs_file, log_file, input_error,
         save_index_file, save_contig_file, save_logging_file):
    if 'Biopython' in sys.modules:
        logging.warning('This assembler using Python module Biopython')
        print('If you want we could help you with this')
        decide = input('Install Biopython y/n?')
        if decide == 'y':
            os.system('pip install Biopython')
        else:
            print('Following work is impossible')
            os.abort()
    iteration = 0
    for_removing = []
    if iteration:
        logging.debug('deep iter')
        file_to_remove = contigassambler(contigs_file, align_file, mid_file, index_file, contigs_file, iteration,
                                         error_description=input_error)
        for_removing.append(file_to_remove)
        iteration += 1
    else:
        logging.debug('first iter')
        file_to_remove = contigassambler(input_file, align_file, mid_file, index_file, contigs_file, iteration,
                                         error_description=input_error)
        for_removing.append(file_to_remove)
        iteration += 1
    if not save_index_file:
        try:
            os.remove(index_file)
            logging.debug('index file removed, dir:' + index_file)
        except FileNotFoundError:
            None
    if not save_contig_file:
        try:
            logging.debug('contigs file removed, dir:' + contigs_file)
            logging.debug(for_removing)
            for i in for_removing:
                os.remove(i)
                os.remove(i + '.nhr')
                os.remove(i + '.nin')
                os.remove(i + '.nsq')
        except FileNotFoundError:
            None
    if not save_logging_file:
        try:
            os.remove(log_file)
            logging.debug('log file removed, dir:' + log_file)
        except FileNotFoundError:
            None
    try:
        os.remove(mid_file)
        os.remove(align_file)
        os.remove(input_fasta_file + '.nhr')
        os.remove(input_fasta_file + '.nin')
        os.remove(input_fasta_file + '.nsq')
    except FileNotFoundError:
        None
    logging.debug('mid file removed, dir:' + mid_file)
    logging.debug('align file removed, dir:' + align_file)
    logging.debug('db file removed, dir:' + input_fasta_file + '.nhr')
    logging.debug('db file removed, dir:' + input_fasta_file + '.nin')
    logging.debug('db file removed, dir:' + input_fasta_file + '.nsq')


if __name__ == '__main__':
    log = working_directory + '/log.log'
    o = open(log, 'w')
    o.close()
    logging.basicConfig(filename=log, level=logging.DEBUG)
    for_align = working_directory + '/align.xml'
    for_indexing = working_directory + '/index_file.fasta'
    for_mid = working_directory + '/mid_file.txt'
    for_contigs = working_directory + '/contigs_file'
    main(input_fasta_file, for_align, for_mid, for_indexing, for_contigs, log,
         input_error=input_error, save_index_file=save_index_file, save_contig_file=save_contig_file,
         save_logging_file=save_logging_file)
