import math

num_test = int(input())
result = []


def helper(n, m, k):
    res = 0
    for i in range(k + 1):
        temp = pow(i, n)
        temp2 = math.comb(m, i)
        res += temp * temp2
    return res


for l in range(num_test):
    nmk = [int(x) for x in input().split()]
    n = nmk[0]
    m = nmk[1]
    k = nmk[2]

    res = helper(n, m, k)

    for p in range(k - 2, 1, -1):
        res = res - (k - 2 - p + 1) * helper(n, m, p)

    result.append(res)

for k in result:
    print(k % 1000000007)


