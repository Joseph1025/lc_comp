n = int(input())
res = 0

for i in range(n):
    line = [int(x) for x in input().split()]
    diag1 = line[i]
    diag2 = line[n - i - 1]
    res += (diag1 - diag2)

print(abs(res))