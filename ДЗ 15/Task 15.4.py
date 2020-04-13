import re


file = 'C:/Python/2430AD.txt'

def high_finder(inp):
    with open(inp, 'r') as f:
        for lines in f:
            for i in re.findall('/[A-Za-z,]*[a-z\s]+!/gi', lines):
                print(i)

high_finder(file)
