class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(0, len(s)):
            if countS.get(s[i]) is None:
                countS[s[i]] = 1
            else:
                countS[s[i]] += 1

            if countT.get(t[i]) is None:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1
        
        for i in range(0, len(s)):
            if countS.get(s[i]) != countT.get(s[i]):
                return False
        
        return True