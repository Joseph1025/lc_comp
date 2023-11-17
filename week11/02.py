def bin_find(lst, x):
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] == x:
            return m
        elif lst[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1


n, k = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
A.sort()
res = 0
sub_index = 0
for i in range(n - 1):
    x = A[i] + k
    j = bin_find(A[sub_index: ], x)
    if j != -1:
        res += 1
        sub_index = j

print(res)
