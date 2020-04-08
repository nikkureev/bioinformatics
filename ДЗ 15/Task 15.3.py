mport re


file = 'C:/Python/2430AD.txt'

# This one will help you to obtain all a-containing words
def a_finder(inp):
    with open(inp, 'r') as f:
        for lines in f:
            for i in re.findall('\w+a\w+', lines):
                print(i)

a_finder(file)
