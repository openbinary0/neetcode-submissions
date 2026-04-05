class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, _ in enumerate(nums):
            for j, _ in enumerate(nums):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []