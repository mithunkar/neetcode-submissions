class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bag = set()
        for num in nums:
            if num in bag:
                return True
            else:
                bag.add(num)
        return False