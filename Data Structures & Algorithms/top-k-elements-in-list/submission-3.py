class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        # Gets the count of each distinct element into a dictionary
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # Creates an array of len(num) + 1 empty arrays
        freq = [[] for i in range(0, len(nums) + 1)]

        for num in counts:
            # Gets the # of occurrences of the num you're looking at
            curr_freq = counts[num]
            # Adds it to our freq array at the index of the count
            freq[curr_freq].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            curr_arr = freq[i]
            for elem in curr_arr:
                res.append(elem)
                if len(res) == k:
                    return res


        # [0,  1,  2,  3,  4,  5,  6]
        # [[], [], [], [], [], [], []]



