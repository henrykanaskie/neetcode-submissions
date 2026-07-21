class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bank = set()
        ascs = [ord(char) for char in s]
        asct = [ord(char) for char in t]
        
        for val in ascs:
            bank.add(val)
        
        for val in asct:
            if val not in bank:
                return False
        
        ssum = sum(ascs)
        tsum = sum(asct)
        print(ssum, tsum)
        if ssum == tsum:
            return True
        
        return False