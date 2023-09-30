num_test = int(input())
res = []

for i in range(num_test):
    lst = list(map(int, input().split()))
    m = lst[0]
    y = lst[1]
    s = lst[2]
    time = y // m
    if time >= s:
        res.append(0)
    else:
        res.append(s - time)

for i in res:
    print(i)
