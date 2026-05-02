from functools import cache

def get_length(s, i):
    length = len(s) - i
    return length if length >= 0 else 0

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            # base case:
            if not get_length(s, i) and not get_length(p, j):
                return True
            if get_length(s, i) and not get_length(p, j):
                return False
            # recursive case (p guaranteed contain characters):
            match = bool(get_length(s, i)) and (s[i] == p[j] or p[j] == ".")
            if get_length(p, j) >= 2 and p[j+1] == "*":
                return dfs(i, j+2) or (match and dfs(i+1, j))
            elif match:
                return dfs(i+1, j+1)
            return False

        return dfs(0, 0)