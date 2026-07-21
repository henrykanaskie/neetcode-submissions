class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            strlen = len(s)
            string += str(strlen) + "#" + s
        return string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s)-1:
            length = "0"
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            word = ""
            k = 0
            while k < length:
                word += s[i + k]
                k += 1
                
            
            i = i + k
            res.append(word)
        
        return res

# 3#the13#ertgidsokfosk5#lover