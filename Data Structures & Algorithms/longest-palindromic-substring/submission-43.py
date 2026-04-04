def get_length(i, j):
    if not (i <= j):
        return 0
    return j - i + 1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = [[None] * len(s) for _ in range(len(s))]

        def dp(i, j):
            # retrieve from cache (if possible):
            if cache[i][j] is not None:
                return cache[i][j]
            # base case:
            if get_length(i, j) == 0:
                return None
            if get_length(i, j) == 1:
                return (i, j)
            # recursive case:
            if s[i] == s[j]:
                inner = dp(i+1, j-1)
                if inner is None:
                    return (i, j)
                (inner_i, inner_j) = inner
                if i+1 == inner_i and j-1 == inner_j:
                    return (i, j)
            left = dp(i+1, j)
            left_length = get_length(*left) if left is not None else 0
            right = dp(i, j-1)
            right_length = get_length(*right) if right is not None else 0
            result = left if left_length >= right_length else right
            # cache and return:
            cache[i][j] = result
            return result

        (i, j) = dp(0, len(s)-1)
        return s[i:j+1]