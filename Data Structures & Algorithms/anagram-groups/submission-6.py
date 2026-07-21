class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            letters = [0 for i in range(26)]
            for c in string:
                letters[ord(c) - ord('a')] += 1
            letters = str(letters)
            if letters in ans:
                ans[letters].append(string)
            else:
                ans[letters] = [string]
        vals = ans.values()
        return list(vals)