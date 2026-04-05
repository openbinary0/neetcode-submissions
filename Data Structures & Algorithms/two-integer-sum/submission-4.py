class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            if num in indices:
                indices[num] += [i]
            indices[num] = [i]
        for i, num in enumerate(nums):
            if target - num in indices:
                value = indices[target - num]
                j = value[0]
                if i == j:
                    continue
                return [i, j]
        return []
