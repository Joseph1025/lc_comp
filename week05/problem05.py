import math

ij = [1, 2]
i = ij[0]
j = ij[1]

root_i = i
root_j = j
found = False
while root_j != root_i or not found:
    if root_j == i or root_i == j:
        found = True
        break
    if root_j != 1:
        root_j = math.floor(root_j / 2)
    if root_i != 1:
        root_i = math.floor(root_i / 2)

if found:
    path = abs(math.floor(math.log(i) / math.log(2)) - math.floor(math.log(j) / math.log(2)))
    print(path)
else:
    i2rt = math.floor(math.log(i) / math.log(2)) - math.floor(math.log(root_i) / math.log(2))
    j2rt = math.floor(math.log(j) / math.log(2)) - math.floor(math.log(root_j) / math.log(2))
    print(i2rt + j2rt)