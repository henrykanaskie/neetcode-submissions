class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        self.length = len(strs)
        for word in strs:
            n = len(word)
            string += str(n)
            string += '#'
            string += word
        return string
    def decode(self, s: str) -> List[str]:
        i = 0
        
        res = []
        while len(res) < self.length:
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            num = int(num)
            dec = ''
            for j in range(num):
                dec += s[i + j + 1]
            i += num + 1
            res.append(dec)

        return res