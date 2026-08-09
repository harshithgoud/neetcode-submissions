class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = nums
        for i,j in enumerate(nums):
            if j in nums[i+1:]:
                return True
        return False

            