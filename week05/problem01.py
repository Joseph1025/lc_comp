
num_test = int(input())
res = []

for i in range(num_test):
    xy = [int(x) for x in input().split()]
    x = xy[0]
    y = xy[1]
    res.append(min(x, y) * 1 + max(0, y - x) * 2)

for i in res:
    print(i)
