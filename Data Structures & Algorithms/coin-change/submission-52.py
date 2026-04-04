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

class Solution:
    # returns minimum number of coins required to reach 'amount'
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [None] * (amount+1)

        def dp(coins, amount):
            # base case:
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            # retrieve from cache:
            if cache[amount] is not None:
                return cache[amount]
            # recursive case:
            min_num_coins = math.inf
            for coin_value in coins:
                num_coins_required = dp(coins, amount - coin_value)
                if num_coins_required < min_num_coins:
                    min_num_coins = num_coins_required
            # store in cache:
            cache[amount] = 1 + min_num_coins
            return cache[amount]

        result = dp(coins, amount)
        return result if result != math.inf else -1