import sys
from typing import List

input = sys.stdin.readline


class Solution:
    def solve(self, n: int, arr: List[int]) -> (int, str):
        """
        B: Return the required string `s` and number `k`.
        """
        # Write your solution in this method.
        res = [0]
        pos = []
        hd = 0
        tl = n - 1
        while hd <= tl and (arr[hd] > res[-1] or arr[tl] > res[-1]):
            if arr[hd] > res[-1] and arr[tl] > res[-1]:
                if arr[hd] < arr[tl]:
                    res.append(arr[hd])
                    hd += 1
                    pos.append('L')
                else:
                    res.append(arr[tl])
                    tl -= 1
                    pos.append('R')
            elif arr[hd] > res[-1]:
                res.append(arr[hd])
                hd += 1
                pos.append('L')
            elif arr[tl] > res[-1]:
                res.append(arr[tl])
                tl -= 1
                pos.append('R')
            else:
                continue
        return len(res) - 1, ''.join(pos)

    def main(self):
        n = int(input())
        arr = list(map(int, input().split()))
        k, s = self.solve(n, arr)
        print(k)
        print(s)


Solution().main()
