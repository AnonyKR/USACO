inputVal = []

x = int(input())
for n in range(x):
    inputVal.append(int(input()))

for n in inputVal:
    if n % 10 == 0:
        print("E")
    else:
        print("B")

