test = int(input())
res = []

for i in range(test):
    n = int(input())
    fuel_lst = list(map(int, input().split()))
    cost_lst = list(map(int, input().split()))
    
    for i in range(n):
        st = fuel_lst[i]
        cost = 0
        for j in range(i, i+n):
            if j >= n:
                j -= n
            
        
