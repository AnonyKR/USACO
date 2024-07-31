with open("herding.in","r") as inVal:
    L = list(inVal)
    intL = [int(x) for x in L[0].split()]
    intL.sort()
    minMove = 0
    maxMove = 0
    if max(intL) - min(intL) != 2:
        if intL[1] - intL[0] == 2 or intL[2] - intL[1] == 2:
            minMove = 1
        else:
            minMove = 2
        if intL[1] - intL[0] > intL[2] - intL[1]:
            maxMove = intL[1] - intL[0] - 1
        else:
            maxMove = intL[2] - intL[1] - 1
    with open("speeding.out", "w") as out:
        print(minMove, file=out)
        print(maxMove, file=out)
    