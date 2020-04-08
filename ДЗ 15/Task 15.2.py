import re


file = 'C:/Python/2430AD.txt'

# This function obtain all numbers from your text file
def refiler(inp):
    with open(inp, 'r') as f:
        for lines in f:
            for i in re.findall('[0-9]{1,}', lines):
                print(i)

refiler(file)
