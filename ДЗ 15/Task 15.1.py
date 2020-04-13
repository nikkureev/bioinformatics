import re


file = 'C:/Theileria_seq/references.txt'
out = 'C:/Theileria_seq/ftps.txt'

# This function obtain all ftps from your file
def refiler(inp, out):
    with open(inp, 'r') as f:
        with open(out, 'w') as d:
            for lines in f:
                d.writelines('\n'.join(re.findall('ftp[.\w+/#]+', lines)))

refiler(file, out)
