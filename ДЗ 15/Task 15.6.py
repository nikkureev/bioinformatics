import re


file = 'C:/Python/2430AD.txt'

# Here you can get all email addresses your file have
def email_finder(inp):
    with open(inp, 'r') as f:
        for lines in f:
            for i in re.findall('\w+@{1}[a-z]+\.[a-z]+', lines):
                print(i)

email_finder(file)
