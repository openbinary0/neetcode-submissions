# Constraints:
# * 1 <= height.length <= 1000
# * 0 <= height[i] <= 1000
# do it layer by layer

"""
   #---#
 #-#---##
 #-##-####
"""

class Solution:
    def create_arr_2d(self, height):
        max_height = max(height)
        arr_2d = [[False] * len(height) for _ in range(max_height)]
        # fill the array:
        for i, h in enumerate(height):
            # h: current height
            # i: height index (current column)
            # loop it column by column
            for row in range(h):
                arr_2d[-(row + 1)][i] = True
        return arr_2d

    def get_filled1(self, row):
        count_water = False
        total_water = 0
        potential_water = 0

        for filled in row:
            # handle start:
            if filled:
                if count_water:
                    total_water += potential_water
                    potential_water = 0
                count_water = True
            elif count_water:
                potential_water += 1
        return total_water

    def get_filled2(self, row):
        start = None
        end = None
        for i in range(len(row)):
            if row[i]:
                start = i
                break
        if start is None:
            return 0
        for i in range(len(row) - 1, -1, -1):
            if row[i]:
                end = i
                break
        return row[start : end + 1].count(False)

    def trap(self, height: List[int]) -> int:
        arr_2d = self.create_arr_2d(height)
        total_filled = 0
        for row in arr_2d:
            total_filled += self.get_filled2(row)
        return total_filled