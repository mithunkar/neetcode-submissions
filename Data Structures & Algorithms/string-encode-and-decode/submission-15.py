class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for elem in strs:
            encoded_str += str(len(elem)) + "#" + str(elem)

        return encoded_str

    # ["neet","code","love","you"]
    
    # "4#neet4#code4#love3#you"

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0

        while(i < len(s)):
            j = i
            while(s[j] != '#'):
                j += 1
            
            word_len = int(s[i:j])
            curr_word = s[j+1 : j+word_len+1]
            res.append(curr_word)
            i = j + word_len + 1

        return res
            

            















