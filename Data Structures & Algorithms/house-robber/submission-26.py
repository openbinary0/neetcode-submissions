# WATCHED SOLUTION!
#
# Deciding whether to rob a house by
# going from left to right and deciding whether
# or not to rob a house has the same permutations
# as iterating from left to right and trying each house
# (and splitting up the problem)

# [1,2,10,1,3,11]
# two decisions: rob current house or go to next
# get the max of those.
# max(nums[0] + rob(nums[2:]), rob(nums[1:]))

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_cache = {}
        return self.rob_houses(nums, 0, rob_cache)

    def rob_houses(self, nums, i, rob_cache):
        # now the problem depends on the index
        # we can easily cache
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