class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left_index = 0
        right_index = len(nums)-1

        while(left_index <= right_index):
            
            curr_index = int((right_index+left_index)/2)
            if nums[curr_index] == target:
                return curr_index
            elif nums[curr_index] < target:
                left_index = curr_index + 1
            elif nums[curr_index] > target:
                right_index = curr_index - 1
        
        return -1