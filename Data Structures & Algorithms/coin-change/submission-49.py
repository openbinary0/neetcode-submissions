import math
import sys
sys.setrecursionlimit(11000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [[None] * (amount+1) for _ in coins]

        def dp(i, amount):
            # base case (initial check):
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            # retrieve from cache (if possible):
            if cache[i][amount] is not None:
                return cache[i][amount]
            # base case:
            if len(coins) - i == 1:
                cache[i][amount] = 1 + dp(i, amount - coins[i])
                return cache[i][amount]
            # recursive case:
            cache[i][amount] = min(1 + dp(i, amount - coins[i]), dp(i+1, amount))
            return cache[i][amount]
            # two operations:
            # * grab the coin and stay
            # * move

        result = dp(0, amount)
        return result if result != math.inf else -1