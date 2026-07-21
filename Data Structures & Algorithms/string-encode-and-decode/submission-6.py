class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        if strs == []:
            return str([])
        rtnstring = ""
        rtnstring = 'ø'.join(strs)
        return rtnstring

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        if s == str([]):
            return []
        stringar = s.split("ø")
        return stringar