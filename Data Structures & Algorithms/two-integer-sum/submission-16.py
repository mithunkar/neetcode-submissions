class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # go through each index in nums

        # check if number in hashmap

        # calculate what number needs to exist in nums based on target

        # add number into hashmap

        seen = {}

        for i in range(0, len(nums)):
            needed = target - nums[i]
            if needed in seen and seen[needed] != i:
                return [min(seen[needed], i), max(seen[needed], i)]
            else:
                seen[nums[i]] = i
