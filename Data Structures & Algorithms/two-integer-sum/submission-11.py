class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        bag = {}

        for i in range(0, len(nums)):
            goal = target - nums[i]
            if goal in bag:
                return [bag[goal], i]
            bag[nums[i]] = i