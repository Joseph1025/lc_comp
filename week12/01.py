num_test = int(input())
res = []

for i in range(num_test):
    s, m = map(int, input().split())
    res.append(s // m)

for i in res:
    print(i)