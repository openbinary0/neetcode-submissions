def get_length(i, j):
    return j - i + 1

class Solution:
    def countSubstrings(self, s: str) -> int:
        cache = [[None] * len(s) for _ in range(len(s))]
        count = 0

        def dp_fill(i, j):
            nonlocal count
            # recurrence relation:
            if i > j:
                return
            if get_length(i, j) == 1:
                cache[i][j] = True
                count += 1
                return
            inner = cache[i + 1][j - 1]
            cache_ij = s[i] == s[j] and (inner or inner is None)
            cache[i][j] = cache_ij
            count += cache_ij

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                dp_fill(i, j)

        return count