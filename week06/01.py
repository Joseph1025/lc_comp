import sys
from typing import List

input = sys.stdin.readline


class Solution:
    def solve(self, n: int, arr: List[int]) -> int:
        """
        A: Return the length of the longest increasing subsequence of
        the new array.

        >>> Solution().solve(7, [1, 6, 5, 4, 2, 3, 7])
        >>> [1, 2, 3, 7]
        """
        # Write your solution in this method.
        return len(set(arr))

    def main(self):
        for _ in range(int(input())):
            n = int(input())
            arr = list(map(int, input().split()))
            print(self.solve(n, arr))


Solution().main()
