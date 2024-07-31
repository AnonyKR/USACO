with open("herding.in","r") as inVal:
    L = list(inVal)
    num = L.pop(0)
    intL = []
    for x in L:
        intL.append(int(x))
    intL.sort()
    minMove = 0
    maxMove = 0
    if max(intL) - min(intL) != num - 1:
        if intL[1] - intL[0] > intL[num-1] - intL[num-2]:
            maxMove = intL[num-2] - num - intL[0] + 2
        else:
            maxMove = intL[num-1] - num - intL[1] + 2
        maxElement = 1
        frontLoc = 0
        endLoc = 0
        currentLoc = intL[0]
        while intL[endLoc] < intL[0] + num:
            maxElement += 1


    with open("herding.out", "w") as out:
        print(minMove, file=out)
        print(maxMove, file=out)
    