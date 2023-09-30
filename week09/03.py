num_test = int(input())
res = []

for i in range(num_test):
    lst = list(map(int, input().split()))
    m = lst[0]
    l = lst[1]  # num of fj in each crate
    arr = list(map(int, input().split()))
    crate = 0
    leftover = 0
    for cons in arr:
        if cons <= leftover:
            leftover -= cons
            leftover -= 1
            leftover = max(0, leftover)
        elif (cons - leftover) % l == 0:
            crate += (cons - leftover) // l
            leftover = 0
        else:
            crate += (cons - leftover) // l + 1
            leftover = l - (cons - leftover) % l - 1
            leftover = max(0, leftover)

    res.append(crate)

for i in res:
    print(i)
