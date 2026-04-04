class Solution:
    def climbStairs(self, n: int) -> int:
        splits_cache = {}
        return 1 + self.numSplits(n, splits_cache)

    def numSplits(self, n, splits_cache):
        # base case:
        if n <= 1:
            return 0
        # recursive case:
        one_step = splits_cache.get(n-1, self.numSplits(n-1, splits_cache))
        two_steps = splits_cache.get(n-2, self.numSplits(n-2, splits_cache))
        splits_n = 1 + one_step + two_steps
        if n not in splits_cache:
            splits_cache[n] = splits_n
        return splits_n