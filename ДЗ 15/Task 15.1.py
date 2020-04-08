import re


file = 'C:/Theileria_seq/references.txt'
out = 'C:/Theileria_seq/ftps.txt'

# This function obtain all ftps from your file
def refiler(inp, out):
    with open(inp, 'r') as f:
        with open(out, 'w') as d:
            for lines in f:
                for i in re.findall('(ftp.(\w+.){9,12}[gz;\t, md5])', lines):
                    d.write(str(i[0]) + '\t')
                d.write('\n')
