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
            max_lis_at_i = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    result = lis(j)
                    if result > max_lis_at_i:
                        max_lis_at_i = result
            return 1 + max_lis_at_i

        max_lis_i = 0
        for i in range(len(nums)):
            lis_i = lis(i)
            if lis_i > max_lis_i:
                max_lis_i = lis_i
        return max_lis_i