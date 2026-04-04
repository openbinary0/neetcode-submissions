import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(coins, amount):
            # base case:
            if amount < 0:
                return math.inf
            if amount == 0:
                return 0
            if len(coins) == 1:
                return 1 + dp(coins, amount - coins[0])
            # recursive case:
            return min(1 + dp(coins, amount - coins[0]), dp(coins[1:], amount))
            # two operations:
            # * grab the coin and stay
            # * move
        
        result = dp(coins, amount)
        return result if result != math.inf else -1