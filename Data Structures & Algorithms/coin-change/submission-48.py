import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(i, amount):
            # base case:
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            if len(coins) - i == 1:
                return 1 + dp(i, amount - coins[i])
            # recursive case:
            return min(1 + dp(i, amount - coins[i]), dp(i+1, amount))
            # two operations:
            # * grab the coin and stay
            # * move

        result = dp(0, amount)
        return result if result != math.inf else -1