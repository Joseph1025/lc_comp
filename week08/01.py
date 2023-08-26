test = int(input())
res = []

for i in range(test):
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    res.append(n * 5 + m * 7)

for i in res:
    print(i)
