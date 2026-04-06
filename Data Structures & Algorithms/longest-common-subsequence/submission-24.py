class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs_current_row = [0] * (len(text2)+1)
        lcs_previous_row = [0] * (len(text2)+1)

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    lcs_current_row[j] = 1 + lcs_previous_row[j+1]
                else:
                    lcs_current_row[j] = max(lcs_previous_row[j], lcs_current_row[j+1])
            lcs_current_row, lcs_previous_row = [0] * (len(text2) + 1), lcs_current_row

        return lcs_previous_row[0]