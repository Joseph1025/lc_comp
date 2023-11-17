# Process Input
t = int(input())
res = []

for i in range(t):
    n = int(input())
    s = str(input())
    stk = []  # Use a stack to track multiple consecutive 1
    maxi = 0  # Records the size of the larget block of 1
    prefix = 0  # Update to the # of preceding 1

    for j in s:
        if j == '1':
            prefix += 1
        else:
            break

    # Count the size of each encountered blocks of 1
    # If size > maxi, update
    for j in s[prefix:]:
        if j == '1':
            stk.append(j)
        else:
            if len(stk) > maxi:
                maxi = len(stk)
            stk = []

    # Empty the stack to get the last block
    if len(stk) > maxi:
        maxi = len(stk)

    res.append(maxi + prefix)

for i in res:
    print(i)

"""
Time Complexity: O(n)
The algorithm iterates through the input string once.
"""