from Bio import SeqIO
from Bio.Seq import Seq


class RNA:

    def __init__(self, input, path=True):
        self.input = input
        # if input is a path to fasta:
        if path:
            self.sequence = SeqIO.parse(input, 'fasta')
        # if input is a sequence:
        else:
            self.sequence = Seq(str(input))

    def do_translation(self):
        return self.sequence.translate()

    def do_reverse_transcription(self):
        return self.sequence.back_transcribe()


print(RNA('AGCTAGCGCTAGCTCGTCGTGCA', False).do_translation())
