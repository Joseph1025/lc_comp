num_test = int(input())
res = []

for i in range(num_test):
    xyz = [int(x) for x in input().split()]
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]

    if z == abs(x + y) or z == abs(x - y):
        res.append("yes")
    else:
        res.append("no")

for i in res:
    print(i)
