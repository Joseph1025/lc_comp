num_test = int(input())
res = []

for i in range(num_test):
    line = list(map(int, input().split()))
    n = line[0]
    m = line[1]
    safe_num = line[2]
    components = []
    for j in range(safe_num):
        line = list(map(int, input().split()))
        x = line[0]
        y = line[1]
        tup = (x, y)
        if len(components) == 0:
            temp = [tup]
            components.append(temp)
        else:
            flag = 0
            for comp in components:
                contain = []
                if x == comp[0] and y == comp[1]+1 or \
                    x == comp[0] and y == comp[1]-1 or \
                    x == comp[0]+1 and y == comp[1] or \
                    x == comp[0]-1 and y == comp[1]:
                    contain.append(flag)
                flag += 1

            if len(contain) == 0:
                temp = [tup]
                components.append(temp)
            elif len(contain) == 1:
                components[contain[0]].append(tup)
            else:
                for k in range(1, len(contain)):
                    components[contain[0]].extend(components[contain[k]])
                    components[contain[k]] = []
                components[contain[0]].append(tup)


