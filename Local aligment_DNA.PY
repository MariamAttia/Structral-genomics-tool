#Mariam Mohamed Attia
#Habiba Mohamed Galal
#jana hany Ahmed
#Ganna allah Ashraf  Mohamed
#Ganna allah khaled Ali
#sarah hatem nabil 

import numpy as np

import string


def local_alignment_DNA(X, Y, gap, match, mismatch):
    m = len(X)
    n = len(Y)
    L = [[0 for x in range(m + 1)] for y in range(n + 1)]  # initialize matrix
    matrix = np.array(L).reshape(n + 1, m + 1)
    print("Initial matrix:")
    print(matrix)
    for i in range(n + 1):
        L[i][0] = 0
    for j in range(m + 1):  # we will make them zero in local
        L[0][j] = 0
        # fill the matrix
        max1 = L[1][1]
    for i in range(1, n + 1, 1):
        for j in range(1, m + 1, 1):
            if X[j - 1] == Y[i - 1]:
                score = match
            else:
                score = mismatch  # up            left        diagonal +(match or mis match)
            L[i][j] = max(L[i - 1][j] + gap, L[i][j - 1] + gap, L[i - 1][j - 1] + score, 0)
            if (L[i][j] >= max1):
                max1 = L[i][j]
                index_i = i
                index_j = j
    print(max1, index_i, index_j)
    matrix = np.array(L).reshape(n + 1, m + 1)
    print("Full matrix:")
    print(matrix)
    print("print final score", max1)  # print final score

    Seq1 = ""
    Seq2 = ""
    LAMatch = ""
    i = index_i  # row 5
    j = index_j  # col 4
    # trace back

    while i > 0 and j > 0:
        up = L[i - 1][j] + gap
        left = L[i][j - 1] + gap
        if X[j - 1] == Y[i - 1]:
            score = match
        else:
            score = mismatch
        diagonal = L[i - 1][j - 1] + score
        if L[i][j] == diagonal:
            Seq1 += X[j - 1]
            Seq2 += Y[i - 1]
            if score == 1:
                LAMatch += "|"
            else:
                LAMatch += " "

            i -= 1
            j -= 1
        elif L[i][j] == up:
            Seq1 += "-"
            LAMatch += " "
            Seq2 += Y[i - 1]
            i -= 1
        else:
            Seq1 += X[j - 1]
            Seq2 += "-"
            LAMatch += " "
            j -= 1

    LAFirst = Seq1[::-1]
    LAMatch = LAMatch[::-1]
    LASecond = Seq2[::-1]

    print(LAFirst)
    print(LAMatch)
    print(LASecond)


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

local_alignment_DNA(X, Y,gap,match,mismatch)
