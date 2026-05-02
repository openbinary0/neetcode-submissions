class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # base case:
        if not s and not p:
            return True
        if s and not p:
            return False
        # recursive case (p guaranteed contain characters):
        if len(p) >= 2 and p[1] == "*":
            if s and (s[0] == p[0] or p[0] == "."):
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            # only one choice:
            return self.isMatch(s, p[2:])
        elif s and (s[0] == p[0] or p[0] == "."):
            return self.isMatch(s[1:], p[1:])
        return False

# s = "accc", p = "a*"
# choices (if there is a match):
# * consume s[0]
# * don't consume s[0], skip