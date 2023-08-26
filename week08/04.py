test = int(input())
res = []

for i in range(test):
    len_a = int(input())
    a = input().split()
    len_b = int(input())
    b = input().split()
    sum_h = 0
    max_h = 0
    sum_t = 0
    max_t = 0
    for i in range(len_a):
        sum_h += int(a[i])
        if sum_h > max_h:
            max_h = sum_h
        sum_t += int(a[len_a - i - 1])
        if sum_t > max_t:
            max_t = sum_t
    
    sum_b = 0
    for i in b:
        if int(i) > 0:
            sum_b += int(i)

    res.append(max(max_h, max_t) + sum_b)

for i in res:
    print(i)
