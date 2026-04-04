# binary tree
# how many split paths are there?

class Solution:
    def climbStairs(self, n: int) -> int:
        splits_cache = {}
        return 1 + self.numSplits(n, splits_cache)

    def numSplits(self, n, splits_cache):
        # base case:
        if n < 2:
            return 0
        # return from cache:
        if n in splits_cache:
            return splits_cache[n]
        # recursive case:
        one_step = self.numSplits(n-1, splits_cache)
        two_steps = self.numSplits(n-2, splits_cache)
        splits_n = 1 + one_step + two_steps
        splits_cache[n] = splits_n
        return splits_n