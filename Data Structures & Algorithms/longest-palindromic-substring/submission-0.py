class Solution:
    def longestPalindrome(self, s: str) -> str:
        residx = 0
        resLen = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j-i + 1):
                        residx = i
                        resLen = j - i + 1
            
        return s[residx : residx + resLen]

