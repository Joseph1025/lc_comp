num_test = int(input())
res = []

for i in range(num_test):
    n = int(input())
    lst = list(map(int, input().split()))
    max_pq = 0
    for preq in lst:
        if preq > max_pq:
            max_pq = preq

    res.append(len(lst) - max_pq)

for i in res:
    print(i)
