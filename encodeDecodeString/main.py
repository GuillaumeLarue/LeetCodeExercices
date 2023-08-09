class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""
        sep = ":;"
        for e in strs:
            s += e
            s += sep
        
        return s


    def decode(self, strs: str) -> List[str]:
        sep = ":;"
        for i in range(len(str)-len(sep)):
            pass