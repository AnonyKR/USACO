def toNum(letter):
    return (ord(letter) - 97)

def toLet(num):
    return chr(num + 97)

def isMoo(strVal):
    if len(strVal) != 3:
        return False
    if strVal[1] == strVal[2]:
        return True
    return False

def toMoo(one, two):
    return "" + toLet(one) + toLet(two) + toLet(two)

with open("mooin.in","r") as inVal:
    L = list(inVal)
    twoNum = L[0].split()
    long = L[1]
    repeat = int(twoNum[0])
    min = int(twoNum[1])
    saveLetter = [] #saveLetter[b][a]
    edge = [] #edge[b][a]
    poss = 0
    possStr = []
    allTrue = []
    for x in range(26):
        temp = []
        temp2 = []
        allTrue.append(True)
        for y in range(26):
            temp.append(0)
            temp2.append(False)
        saveLetter.append(temp)
        edge.append(temp2)
    for n in range(repeat - 2):
        subStr = long[n:n+3]
        if isMoo(subStr):
            temp = edge[toNum(subStr[1])][toNum(subStr[0])]
            edge[toNum(subStr[1])] = allTrue
            edge[toNum(subStr[1])][toNum(subStr[0])] = temp
            saveLetter[toNum(subStr[1])][toNum(subStr[0])] += 1
        else:
            if subStr[0] == subStr[1]:
                if n < repeat - 3:
                    if subStr[2] != long[n + 3]:
                        edge[toNum(subStr[2])][toNum(subStr[0])] = True
            else:
                edge[toNum(subStr[2])][toNum(subStr[0])] = True
            if subStr[0] == subStr[2]:
               if n < repeat - 4:
                    if long[n + 4] != long[n + 3]:
                        edge[toNum(subStr[1])][toNum(subStr[0])] = True 
            else:
                edge[toNum(subStr[1])][toNum(subStr[0])] = True
    for n in range(26):
        for m in range(26):
            if n != m:
                if saveLetter[m][n] >= min:
                    poss += 1
                    possStr.append(toMoo(n,m))
                elif saveLetter[m][n] + 1 == min:
                    if edge[m][n]:
                        poss += 1
                        possStr.append(toMoo(n,m))
    with open("mooin.out", "w") as out:
        out.write("" + poss + "\n")
        for i in possStr:
            out.write("" + i + "\n")