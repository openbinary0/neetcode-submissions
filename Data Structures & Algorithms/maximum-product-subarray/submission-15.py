# * if only one element: return it
# count negative integers:
# * if even: return the product of all integers in the array
# * if odd: remove one negative integer and compare
#   the two subarrays left and right.
#   * break down the problem further?
# * Can the max product be negative? Only with one negative element
# * Count the parity on either side of the removed negative integer
# * Max is only possible when parity is even on either side
#   (current negative integer index is odd: 1st negative, 3rd, etc)
# * Cache?
# * Store indices of every negative number.
# * zeroes are possible!!!!!!!!!!

import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums_arrays = self.split_zeroes(nums)
        has_zeroes = False
        for num in nums:
            if num == 0:
                has_zeroes = True
                break

        max_product = -math.inf
        for num_array in nums_arrays:
            result = self.maxProduct2(num_array)
            if result > max_product:
                max_product = result
        return 0 if max_product < 0 and has_zeroes else max_product

    # does not take into account zeroes
    def maxProduct2(self, nums):
        if len(nums) == 1:
            return nums[0]

        negative_indices = []
        for i, num in enumerate(nums):
            if num < 0:
                negative_indices.append(i)

        if len(negative_indices) % 2 == 0:
            # multiply all elements and return:
            return math.prod(nums)

        largest_product = -math.inf
        for nth_index, negative_index in enumerate(negative_indices):
            if nth_index % 2 != 0:
                continue
            # even nth_index:
            left = math.prod(nums[:negative_index])
            right = math.prod(nums[negative_index+1:])
            max_lr = max(left, right)
            if max_lr > largest_product:
                largest_product = max_lr
        return largest_product

    def split_zeroes(self, nums):
        nums_arrays = []
        array_start = None
        in_array = False

        for i, num in enumerate(nums):
            # handle start:
            if num != 0 and not in_array:
                in_array = True
                array_start = i

            # handle end:
            if in_array and num == 0:
                array_end = i - 1
                if array_start is not None:
                    nums_arrays.append(nums[array_start : array_end + 1])
                in_array = False
            elif in_array and i + 1 == len(nums):
                array_end = i
                if array_start is not None:
                    nums_arrays.append(nums[array_start : array_end + 1])
        return nums_arrays