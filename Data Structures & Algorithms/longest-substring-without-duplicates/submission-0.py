class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        unique = set()
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1

            unique.add(s[r])
            longest = max(longest, r - l + 1)
        return longest


