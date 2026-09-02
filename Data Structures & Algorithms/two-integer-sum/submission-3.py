class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        locations = {}
        
        for i in range(0, len(nums)):
            
            curr_num = nums[i]
            num_wanted = target - nums[i]

            if num_wanted in locations:
                return [min(i, locations[num_wanted]), max(i, locations[num_wanted])]
            else:
                locations[curr_num] = i

