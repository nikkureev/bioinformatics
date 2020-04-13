import re
import matplotlib.pyplot as plt


file = 'C:/Python/2430AD.txt'

# Word's length distribution graph maker
def wldgm(inp):
    s = []
    with open(inp, 'r') as f:
        for lines in f:
            ar = re.search('([A-z]\w+)(?!.*\1)', lines)
            if ar != None:
                s.append(ar.group())
    return s


x = refiler(file)
y = [len(i) for i in x]
fig, ax = plt.subplots()
ax.set_xticklabels(labels=x, rotation = 45)
ax.bar(x, y)
plt.show()
