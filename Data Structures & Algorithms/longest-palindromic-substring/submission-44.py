# Goal: return the longest palindromic substring of 's'
# Examples:
# "abadef" => "aba"
# "abbadef" => "abba"
# "llllabbadef" => "abba"

# "aba"
# 0, 0.5, 1, 1.5, 2

# Strategies:
# * odd and even
# * Keep two indices: start and end
#   * Work with indices instead of strings
# * Decisions???

# Pseudocode:
# * Loop through s from i to j
#   * For each char in s:

import math

class Solution:
    def longest_palindrome_at(self, si, s):
        i = math.floor(si)
        j = math.ceil(si)
        if s[i] != s[j]:
            return (0, 0)
        while i-1 >= 0 and j+1 <= len(s)-1 and s[i-1] == s[j+1]:
            i -= 1
            j += 1
        return (i, j)

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest_palindrome_length = 0
        longest_palindrome_indices = (0, 0)
        si = 0
        while si <= len(s)-1:
            (i, j) = self.longest_palindrome_at(si, s)
            length = j - i + 1
            if length > longest_palindrome_length:
                longest_palindrome_indices = (i, j)
                longest_palindrome_length = length
            si += 0.5
        (i, j) = longest_palindrome_indices
        return s[i:j+1]