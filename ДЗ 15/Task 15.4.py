import re


file = 'C:/Python/2430AD.txt'

def high_finder(inp):
    with open(inp, 'r') as f:
        for lines in f:
            for i in re.findall('[A-Z]{1}[a-z\s]+!', lines):
                print(i)

high_finder(file)
