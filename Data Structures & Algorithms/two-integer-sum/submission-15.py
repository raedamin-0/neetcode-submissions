class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums and i != nums.index(difference):
                return sorted([i, nums.index(difference)])
        return [-1]