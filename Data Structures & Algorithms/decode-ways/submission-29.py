def get_next(s, si):
    if int(s[si:si+2]) <= 26:
        return (si+1, si+2)
    return (si+1,)

class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dp(s, si):
            # base case:
            if s[si] == "0":
                return 0
            if len(s) - si == 1:
                return 1
            if len(s) - si == 2:
                return 2 if int(s[si:si+2]) <= 26 and s[si+1] != "0" else 1
            # retrieve from cache:
            if si in cache:
                return cache[si]
            # recursive case:
            next = get_next(s, si)
            if len(next) == 1:
                (next1,) = next
                result = dp(s, next1)
                cache[si] = result
                return result
            (next1, next2) = next
            result = dp(s, next1) + dp(s, next2)
            cache[si] = result
            return result

        return dp(s, 0)