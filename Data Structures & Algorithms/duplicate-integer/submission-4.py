class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current = set({})
        for num in nums:
            if num in current:
                return True
            else:
                current.add(num)
        return False