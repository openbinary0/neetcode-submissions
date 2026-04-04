class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_cache1 = {}
        rob_cache2 = {}
        return max(
            self.rob_houses(nums, 1, rob_cache1),
            nums[0] + self.rob_houses(nums[2:-1], 0, rob_cache2)
        )

    def rob_houses(self, nums, i, rob_cache):
        # now the problem depends only on the index,
        # we can easily cache
        # alternative: use an array instead of
        # a dictionary for the cache (slightly faster)
        if i >= len(nums):
            return 0
        if i in rob_cache:
            return rob_cache[i]
        best_robbed = max(
            nums[i] + self.rob_houses(nums, i+2, rob_cache),
            self.rob_houses(nums, i+1, rob_cache)
        )
        rob_cache[i] = best_robbed
        return best_robbed