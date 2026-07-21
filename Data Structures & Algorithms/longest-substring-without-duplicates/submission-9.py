class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        substring = set()
        for r in range(len(s)):
            while s[r] in substring:
                
                substring.remove(s[l])
                l += 1
                          
            longest = max(longest, r - l + 1)
            substring.add(s[r])

        return longest