from functools import cache

def get_length(s, i):
    length = len(s) - i
    return length if length >= 0 else 0

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def is_match(i, j):
            # base case:
            if not get_length(s, i) and not get_length(p, j):
                return True
            if get_length(s, i) and not get_length(p, j):
                return False
            # recursive case (p guaranteed contain characters):
            if get_length(p, j) >= 2 and p[j+1] == "*":
                if get_length(s, i) and (s[i] == p[j] or p[j] == "."):
                    return is_match(i+1, j) or is_match(i, j+2)
                # only one choice:
                return is_match(i, j+2)
            elif get_length(s, i) and (s[i] == p[j] or p[j] == "."):
                return is_match(i+1, j+1)
            return False

        return is_match(0, 0)