with open("speeding.in","r") as inVal:
    L = list(inVal)
    nums = [int(x) for x in L[0].split()]
    N = []
    M = []
    Ndone = False
    for x in range(len(L)-1):
        if not Ndone:
            N.append([int(x) for x in L[x+1].split()])
            if x+1 >= nums[0]:
                Ndone = True
        else:
            M.append([int(x) for x in L[x+1].split()])
    Ncount = 1
    Nsum = N[Ncount-1][0]
    Mcount = 1
    Msum = M[Mcount-1][0]
    maxDif = 0
    while True:
        if N[Ncount-1][1] < M[Mcount-1][1]:
            if M[Mcount-1][1] - N[Ncount-1][1] > maxDif:
                maxDif = M[Mcount-1][1] - N[Ncount-1][1]
        if Nsum == 100 and Msum == 100:
            break
        if Nsum == Msum:
            Ncount += 1
            Mcount += 1
            Nsum += N[Ncount-1][0]
            Msum += M[Mcount-1][0]
        elif Nsum > Msum:
            Mcount += 1
            Msum += M[Mcount-1][0]
        else:
            Ncount += 1
            Nsum += N[Ncount-1][0]
    with open("speeding.out", "w") as out:
        print(maxDif, file=out)