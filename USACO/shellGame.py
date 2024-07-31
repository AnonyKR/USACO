with open("shell.in","r") as inVal:
    L = list(inVal)
    repeat = int(L[0])
    point = [0,0,0]
    loc = [0,1,2]
    for x in range(repeat):
        nums = [int(x) for x in L[x+1].split()]
        temp = loc[nums[0]-1]
        loc[nums[0]-1] = loc[nums[1]-1]
        loc[nums[1]-1] = temp
        point[loc[nums[2]-1]] += 1
    with open("shell.out", "w") as out:
        print(max(point), file=out)