import numpy as np


def global_alignment_DNA(X, Y, gap, match, mismatch):
    m = len(X)
    n = len(Y)
    L = [[0 for x in range(m + 1)] for y in range(n + 1)]  # initialize matrix
    matrix = np.array(L).reshape(n + 1, m + 1)
    print("Initial matrix:")
    print(matrix)
    for i in range(n + 1):
        L[i][0] = (i*gap)
    for j in range(m + 1):  # we will make them zero in local
        L[0][j] = (j*gap)
        # fill the matrix
    for i in range(1, n + 1, 1):
        for j in range(1, m + 1, 1):
            if X[j - 1] == Y[i - 1]:
                score = match
            else:
                score = mismatch  # up            left        diagonal +(match or mis match)
            L[i][j] = max(L[i - 1][j] + gap, L[i][j - 1] + gap, L[i - 1][j - 1] + score)
    matrix = np.array(L).reshape(n + 1, m + 1)
    print("Full matrix:")
    print(matrix)
    print("print final score", L[n][m])  # print final score

    GAFirst = ""
    GASecond = ""
    GAMatch = ""
    i = n  # row 5
    j = m  # col 4
    # trace back
    while i > 0 and j > 0:
        up = L[i - 1][j] - gap
        left = L[i][j - 1] - gap
        if X[j - 1] == Y[i - 1]:
            score = match
        else:
            score = mismatch
        diagonal = L[i - 1][j - 1] + score
        if L[i][j] == diagonal:
            GAFirst += X[j - 1]
            GASecond += Y[i - 1]
            if score == 1:
                GAMatch += "|"
            else:
                GAMatch += " "
            i -= 1
            j -= 1
        elif L[i][j] == up:
            GAFirst += "-"
            GAMatch += " "
            GASecond += Y[i - 1]
            i -= 1
        else:
            GAFirst += X[j - 1]
            GASecond += "-"
            GAMatch += " "
            j -= 1

    while (i > 0):
        GAFirst += "-"
        GASecond += Y[i - 1]
        GAMatch += " "
        i -= 1
    while (j > 0):
        GAFirst += X[j - 1]
        GASecond += "-"
        GAMatch += " "
        j -= 1

    GAFirst = GAFirst[::-1]
    GAMatch = GAMatch[::-1]
    GASecond = GASecond[::-1]

    print(GAFirst)
    print(GAMatch)
    print(GASecond)


# calling the function
X = " "
Y = " "
gap= 0
match=0
mismatch=0
X=input("First sequence:")
Y=input("Second sequence:")
gap=int(input("GAP:"))
match=int(input("Match:"))
mismatch=int(input("Mismatch:"))

global_alignment_DNA(X, Y, gap,match,mismatch)
