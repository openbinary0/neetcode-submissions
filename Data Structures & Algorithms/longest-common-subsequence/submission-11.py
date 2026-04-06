# lcs("ab", "zb") =
# max(lcs("b", "zb"), lcs("ab", "b"))

from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    lcs[i][j] = 1 + lcs[i+1][j+1]
                else:
                    lcs[i][j] = max(lcs[i+1][j], lcs[i][j+1])

        return lcs[0][0]