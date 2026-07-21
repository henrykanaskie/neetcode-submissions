class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isanagram(s1, s2):
            wordbank1 = {}
            wordbank2 = {}
            if len(s1) != len(s2):
                return False
            for char in s1:
                if char in wordbank1:
                    wordbank1[char] += 1
                else:
                    wordbank1[char] = 1
            for char in s2:
                if char in wordbank2:
                    wordbank2[char] += 1
                else:
                    wordbank2[char] = 1
                    
            return wordbank1 == wordbank2
        
        anagram = []
        notused = strs
        removedlist = []
        indices = set()
        for i,string in enumerate(strs):
            if i in indices:
                continue
            stringlist = []
            for j, strings in enumerate(notused):
                if isanagram(string, strings) and j not in indices:
                    stringlist.append(strings)
                    indices.add(j)
            
            if len(stringlist) > 0:
                anagram.append(stringlist)
        
        return anagram

        