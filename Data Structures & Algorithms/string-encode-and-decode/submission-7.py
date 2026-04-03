class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "$" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0 #counter for each char in s
        res = []

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            
            k = int(s[i:j])
            res.append(s[j + 1 : j + 1 + k])
            i = j + 1 + k

        return res


