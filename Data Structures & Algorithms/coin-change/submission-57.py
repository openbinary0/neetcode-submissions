# * 1D dynamic programming
#   * overlapping subproblems
#   * optimal substructure
# * Example: [1, 3, 4, 5]
# * coins doesn't change
# * number of edges is the amount of coins.
#   We want to find the path to 0 with the least edges.

# 1. find the path with the least edges

import math
import sys
sys.setrecursionlimit(11000)

# BOTTOM-UP APPROACH:
# dp[0] = 0
# dp[7] = 1 + min(dp[7-1], dp[7-3], dp[7-4], dp[7-5])
# fill cache from lowest to highest. If dp[x] isn't possible,
# set it to infinity
# pre-fill the cache with math.inf

class Solution:
    # returns minimum number of coins required to reach 'amount'
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [math.inf] * (amount+1)
        cache[0] = 0

        def fill_cache(i):
            min_num_coins = math.inf
            for coin_value in coins:
                if i - coin_value < 0:
                    continue
                num_coins_required = cache[i - coin_value]
                if num_coins_required < min_num_coins:
                    min_num_coins = num_coins_required
            cache[i] = 1 + min_num_coins

        for i in range(1, amount+1):
            fill_cache(i)

        return cache[amount] if cache[amount] != math.inf else -1