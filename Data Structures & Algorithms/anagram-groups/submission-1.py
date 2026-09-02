class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = {}

        for string in strs:
            freq_table = [0] * 26
            for letter in string:
                location = ord(letter) - ord('a')
                print(location)
                freq_table[location] += 1
            freq_table = tuple(freq_table)
            if freq_table in anagram_map:
                anagram_map[freq_table].append(string)
            else:
                anagram_map[freq_table] = [string]

        
        res = []

        for key in anagram_map:
            res.append(anagram_map[key])
        
        return res