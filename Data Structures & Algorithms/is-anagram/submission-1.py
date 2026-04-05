class Solution:
    def count_chars(self, s):
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        return count

    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_chars(s) == self.count_chars(t)
        # count characters in s
