# * 2D DP problem. Each state is defined by m, n
#   * 1 <= m, n <= 100
# * how to split up into subproblems?
# * Top-left: grid[0][0], bottom-right: grid[m - 1][n - 1]
# * Same number of paths for m x n and n x m.
# * Play around with the problem

from functools import cache

class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        # base case:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)