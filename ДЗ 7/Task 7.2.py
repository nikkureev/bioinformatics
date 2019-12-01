from Bio import SeqIO


def align(path_in, match_score, miss_match_score, gap_score):
    sequences = []
    for record in SeqIO.parse(path_in, "fasta"):
        sequences.append(record.seq)
    matrix = [[0 for i in range(len(sequences[0]) + 1)] for j in range(len(sequences[1]) + 1)]

    matrix[0] = [i for i in range(len(matrix[0]))]

    n = 0
    for i in matrix:
        i[0] = n
        n += 1

    d = gap_score
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if sequences[0][j - 1] == sequences[1][i - 1]:
                g = match_score
            else:
                g = miss_match_score
            matrix[i][j] = min(matrix[i - 1][j - 1] + g, matrix[i - 1][j] + d, matrix[i][j - 1] + d)

    score = 0
    seq = []
    i = len(matrix) - 1
    j = len(matrix[0]) - 1

    while i != 0 or j != 0:
        if min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) == matrix[i - 1][j - 1]:
            seq.append([str(sequences[1][i - 1]), str(sequences[0][j - 1])])
            i -= 1
            j -= 1
            score += matrix[i - 1][j - 1]
        elif min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) == matrix[i][j - 1]:
            seq.append(['-', str(sequences[0][j - 1])])
            i = i
            j -= 1
            score += matrix[i][j - 1]
        elif min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) == matrix[i - 1][j]:
            seq.append([str(sequences[1][i - 1]), '-'])
            i -= 1
            j = j
            score += matrix[i - 1][j]

    s1 = ''
    seq.reverse()
    for i in seq:
        s1 += str(i[0])
    s2 = ''
    print()
    for i in seq:
        s2 += str(i[1])

    align_result = (score, s1, s2)
    return align_result
