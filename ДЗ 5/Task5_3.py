squares = [i * i for i in range(11)]

sums = [i + [j for j in range(5, 9)][i] for i in range(4)]

n = ['A', 'T', 'G', 'C']
changes = [[str(n[k]) + '->' + str([j for j in n][i]) for i in range(4) if n[k] != [j for j in n][i]] for k in range(4)]

matrix = [[i for i in range(a, b)] for a, b in [[0, 3], [3, 6], [6, 9]]]
