from Bio import SeqIO


class rna:

    def __init__(self, input):
        self.input = input
        # if input is a sequence:
        if type(self.input) == str:
            self.seq = input

        # if input is a path to fasta:
        else:
            self.seq = SeqIO.parse(input, 'fasta')

    def do_translation(self):
        return self.seq.translate()

    def do_reverse_transcription(self):
        return self.seq.back_transcribe()
