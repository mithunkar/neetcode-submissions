class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            
            counts = [0] * 26
            
            for letter in word:
                position = ord(letter) - ord("a")
                counts[position] += 1

            counts = tuple(counts)

            if counts not in groups:
                groups[counts] = [word]
            else:
                groups[counts].append(word)

        return groups.values()