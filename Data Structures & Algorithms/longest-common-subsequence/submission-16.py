class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Ensure text2 is the longer one to use less space
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)  # previous row
        curr = [0] * (n + 1)  # current row

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            # Move current row to prev for next iteration
            prev, curr = curr, [0] * (n + 1)

        return prev[n]