class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:     # look thru each string
            key = [0] * 26   # list key of characters 
            for char in s:  # go thru each char
                key[ord(char)-ord('a')] += 1 #increment key at correct location based on char
            res[tuple(key)].append(s)
        
        return list(res.values())