# Mariam Mohamed Attia
# Habiba Mohamed Galal
# jana hany Ahmed
# Ganna allah Ashraf  Mohamed
# Ganna allah khaled Ali
# sarah hatem nabil


# replaces repetition with XS

def listofXinsteadofrepetion(Query):
    removedtlist = [Query[0], Query[1]]
    # we remove repetion of 2
    for n in range(0, len(Query) - 4, 2):
        if getscore(Query[n], Query[n]) == getscore(Query[n + 2], Query[n + 2]) :
              if  getscore(Query[n + 1],Query[n + 1]) == getscore(Query[n + 3], Query[n + 3]):
                  removedtlist.append('X')
                  removedtlist.append('X')
              else:

                   removedtlist.append(Query[n+2])
                   removedtlist.append(Query[n+3])

        else:

            removedtlist.append(Query[n+2])
            removedtlist.append(Query[n+3])
    removedtlist.append(Query[len(Query) - 2])
    removedtlist.append(Query[len(Query) - 1])


    return removedtlist



def getscore(a1, a2):
    i = aminoAcids[a1]
    j = aminoAcids[a2]
    return BlosumList[i][j]


def split(Querybefore):
    return [char for char in Querybefore]


# repetiton removing
def modificationofquery(removedtlist):
    Modified = []
    for o in range(len(removedtlist)):
        if removedtlist[o] != 'X':
            Modified.append(Query[o])


    return Modified


# words extraction
def words(modified, wordlength):
    listofwordss = []

    for i in range(0, len(modified) - (wordlength - 1)):
        word = modified[i:i + wordlength]
        # Modified2 = "".join(word)
        listofwordss.append([word, i])

    return listofwordss


def seedextraction(listofwordss, threshold):
    Seeds = []
    for i in range(0, len(listofwordss)):
        oneword = list(listofwordss[i][0])
        s = list(listofwordss[i][0])
        for k in range(0, len(s)):
            for j in range(0, len(listP)):
                oneword[k] = listP[j]
                # score = getscore(oneword, s)
                Score = int(getscore(s[0], oneword[0]) + getscore(s[1], oneword[1]) + getscore(s[2], oneword[2]))
                if Score >= threshold:
                    Seeds.append(["".join(oneword), Score, listofwordss[i][1]])

                oneword = s

    return Seeds


# def checkifprotien (Query):


def hit_seed(seeds, db, wordlength):
    hitList = []
    for i in range(0, len(seeds)):
        seed_letter = seeds[i][0]
        for j in range(0, len(db)):
            if db[j:j + wordlength] == seed_letter:
                hitList.append([i, j])
    return hitList


def Extend(hit_list, db, seeds, Query):
    hsp = []

    for i in range(0, len(hit_list)):

        leftIndex = hit_list[i][1] - 1
        rightIndex = leftIndex + 4
        seedIndex = hit_list[i][0]
        leftIndexQuery = seeds[seedIndex][2] - 1
        rightIndexQuery = leftIndexQuery + 4
        score = seeds[seedIndex][1]
        mxScore = score
        while (mxScore - score < threshold2):  # terminating condition
            if leftIndex >= 0 and leftIndexQuery >= 0:
                score += getscore(db[leftIndex], Query[leftIndexQuery])
                leftIndexQuery -= 1
                leftIndex -= 1

            # ata2ked eno ma5les4y
            if rightIndex < len(db) and rightIndexQuery < len(Query):
                score += getscore(db[rightIndex], Query[rightIndexQuery])
                rightIndex += 1
                rightIndexQuery += 1

            # yemen hwa elmkamel we el4emal mafe4 gambo haga
            # if leftIndexQuery < 0:
            if rightIndexQuery >= len(Query) or rightIndex >= len(db):  # len query 5eles
                break
            # if leftIndex < 0:
            if rightIndex >= len(db) or rightIndexQuery >= len(Query):
                break
            if mxScore < score:
                mxScore = score
        hsp.append([rightIndex - 1, leftIndex + 1, rightIndexQuery - 1, leftIndexQuery + 1, score])
    return hsp


with open('Blosum62.txt', 'r') as in_file:
    lines = in_file.read().splitlines()
    BlosumList = []
    for line in lines:
        temp = [int(i) for i in line.split()]
        BlosumList.append(temp)
in_file.close
aminoAcids = {'A': 0, 'R': 1, 'N': 2, 'D': 3, 'C': 4, 'Q': 5, 'E': 6, 'G': 6, 'H': 7, 'I': 8, 'L': 9, 'K': 10, 'M': 11,
              'F': 12, 'P': 13, 'S': 14, 'T': 15, 'W': 16, 'Y': 17, 'V': 18, 'B': 19, 'Z': 20, 'X': 21}
# Query = ['A', 'T', 'A', 'T', 'T', 'C', 'D', 'H']
listP = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'B']

# print (BlosumList)

Querybefore = input("please enter the query")
Query_upper=Querybefore.upper()
Query = split(Query_upper)



wordlengthstr = input("Please Enter The Word Length  : ")
wordlength = int(wordlengthstr)

threshold = int(input("Enter the Word Threshold : "))
threshold2 = int(input("Enter HSP Threshold : "))

removedlist = listofXinsteadofrepetion(Query)


modified = modificationofquery(removedlist)
listofwordss = words(modified, wordlength)
print(listofwordss)
seeds = seedextraction(listofwordss, threshold)
print(seeds)
print(len(seeds))
print(modified)
db = ['ATCCGATCGATCGATCGATCG', 'ATCCGATCGATCGATCGATCG']
for index, dbseq in enumerate(db):
    hit_list = hit_seed(seeds, dbseq, wordlength)
    print("Hit_List : ", hit_list)
    hsp_List = Extend(hit_list, dbseq, seeds, Query)
    print("Hsp_List : ", hsp_List)
    if len(hsp_List) == 0:
        print("Query Not found ")
    else:
        total_hsp = 0
        for i in range(0, len(hsp_List)):
            total_hsp += hsp_List[i][4]
        print('seq', index + 1, ':', total_hsp)
print(removedlist)
