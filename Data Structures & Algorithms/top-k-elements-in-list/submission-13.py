class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # have a hash map
        counts = {}

        # each key is a new number encountered
        for num in nums:
            if num not in counts: # add to hashmap
                counts[num] = 1
            else: # increment count
                counts[num] += 1
        
        res= sorted(list(counts.items()), key=lambda x: x[1], reverse=True)[0:k]
        actual_res = []
        for item in res:
            actual_res.append(item[0])
        return actual_res


