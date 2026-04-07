# bottom-up approach: start at end and go to i=0

from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def lis(i): # lis starting at i
            # base case:
            if len(nums) - i <= 1:
                return len(nums) - i
            # find all indices larger than nums[i]
            max_lis_from_i = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    lis_j = lis(j)
                    if lis_j > max_lis_from_i:
                        max_lis_from_i = lis_j
            return 1 + max_lis_from_i

        return max((lis(i) for i in range(len(nums))), default=0)