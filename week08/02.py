"""
Jimmy has two strings: 
W and M. Print "YES" (without quotes) if W is a subsequence of 
M or if M is a subsequence of W. Otherwise, print "NO".
"""

test = int(input())
res = []

for i in range(test):
    arr = input().split()
    w = arr[0]
    m = arr[1]
    if len(w) > len(m):
        ind_m = 0
        ind_w = 0
        while ind_m < len(m) and ind_w < len(w):
            if m[ind_m] == w[ind_w]:
                ind_m += 1
            ind_w += 1
        if ind_m == len(m):
            res.append("YES")
        else:
            res.append("NO")
    else:
        # len(w) <= len(m)
        ind_m = 0
        ind_w = 0
        while ind_m < len(m) and ind_w < len(w):
            if m[ind_m] == w[ind_w]:
                ind_w += 1
            ind_m += 1
        if ind_w == len(w):
            res.append("YES")
        else:
            res.append("NO")

for i in res:
    print(i)
