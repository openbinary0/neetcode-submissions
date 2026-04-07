# wordDict = ["cats","cat","sin","in","car"]
# wordBreak("catsincars") =
# * wordBreak("incars") or wordBreak("sincars")

from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(i):
            # * loop through wordDict and find
            #   if 's' starts with any of the words
            # * if so, remove it and run dfs on the
            #   string without the prefix
            # base case:
            if len(s) - i <= 0:
                return True
            # recursive case:
            for word in wordDict:
                if s.startswith(word, i) and dfs(i+len(word)):
                    return True
            return False

        return dfs(0)