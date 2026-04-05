class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            if num not in indices:
                indices[num] = i
        for i, num in enumerate(nums):
            if target - num in indices:
                j = indices[target - num]
                if i == j:
                    continue
                return [i, j] if j > i else [j, i]
        return []
