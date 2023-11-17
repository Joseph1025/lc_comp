t = int(input())
res = []

for i in range(t):
    n, u, d = map(int, input().split())
    h_lst = list(map(int, input().split()))
    para = True
    j = 0
    while j < n - 1:
        if 0 < h_lst[j + 1] - h_lst[j] <= u:
            j += 1
        elif h_lst[j + 1] == h_lst[j]:
            j += 1
        elif h_lst[j] > h_lst[j + 1]:
            if h_lst[j] - h_lst[j + 1] <= d:
                j += 1
            else:
                if para:
                    j += 1
                    para = False
                else:
                    break
        else:
            break
    res.append(j + 1)

for i in res:
    print(i)