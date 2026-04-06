class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "$" + s
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        decoded = []
        while l < len(s):
            while s[r] != "$":
                r += 1
            #if we are here r is pointing to "$" deliminator
            x = int(s[l:r])
            r += 1
            decoded.append(s[r: r + x])
            l = r + x
            r = l
        return decoded


            