from Bio import SeqIO
import matplotlib.pyplot as plt


def align(path_in, match_score, miss_match_score, gap_score, glob_align=True):
    sequences = []
    for record in SeqIO.parse(path_in, "fasta"):
        sequences.append(record.seq)
    matrix = [[0 for i in range(len(sequences[0]) + 1)] for j in range(len(sequences[1]) + 1)]

    matrix[0] = [i for i in range(len(matrix[0]))]

    if glob_align:
        n, m = gap_score, gap_score
    else:
        n, m = 0, 0
    for i in matrix:
        i[0] = n
        n += m

    d = gap_score
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if sequences[0][j - 1] == sequences[1][i - 1]:
                g = match_score
            else:
                g = miss_match_score
            if glob_align:
                matrix[i][j] = min(matrix[i - 1][j - 1] + g, matrix[i - 1][j] + d, matrix[i][j - 1] + d)
            else:
                if min(matrix[i - 1][j - 1] + g, matrix[i - 1][j] + d, matrix[i][j - 1] + d) > 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = -1

    for i in matrix:
        print(i)
    score = 0
    seq = []
    i = len(matrix) - 1
    j = len(matrix[0]) - 1

    coordinates = [[i, j]]
    while i > 0 or j > 0:
        if min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) == matrix[i - 1][j - 1]:
            seq.append([str(sequences[1][i - 1]), str(sequences[0][j - 1])])
            i -= 1
            j -= 1
            score += matrix[i - 1][j - 1]
            coordinates.append([i - 1, j - 1])
        elif min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) == matrix[i][j - 1]:
            seq.append(['-', str(sequences[0][j - 1])])
            i = i
            j -= 1
            score += matrix[i][j - 1]
            coordinates.append([i - 1, j])
        elif min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) == matrix[i - 1][j]:
            seq.append([str(sequences[1][i - 1]), '-'])
            i -= 1
            j = j
            score += matrix[i - 1][j]
            coordinates.append([i, j - 1])

    coordinates.sort()
    #coordinates.remove([-1, -1])
    x, y = [], []
    for i in coordinates:
        x.append(i[0])
        y.append(i[1])
    fig = plt.subplot()
    fig.plot(x, y)
    fig.minorticks_on()
    fig.grid(which='major')
    fig.grid(which='minor')
    plt.show()

    s1 = ''
    seq.reverse()
    for i in seq:
        s1 += str(i[0])
    s2 = ''
    print()
    for i in seq:
        s2 += str(i[1])

    align_result = (score, s1.upper(), s2.upper())
    return align_result


result = align('C:/Theileria/seq2.txt', -2, 3, 2, glob_align=True)
print(result[0], result[1], result[2], sep='\n')
