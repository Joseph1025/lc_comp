"""
Jimmy has a binary string. In one move, he can perform one of the following operations:

Delete one character. e.g., 0010 -> 000 by deleting the third character.
Flip all characters in the string. e.g., 0010 -> 1101.
What is the minimum number of operations required to make all characters of the string equal to 0?
"""

test = int(input())
res = []

for i in range(test):
    digit = int(input())
    string_number = input()
    count1 = string_number.count('1')
    count0 = string_number.count('0')
    if count1 == 0:
        res.append(0)
    elif count0 > count1:
        res.append(count1)
    elif count0 == count1:
        res.append(count0)
    else:
        res.append(count0 + 1)
    

for i in res:
    print(i)


