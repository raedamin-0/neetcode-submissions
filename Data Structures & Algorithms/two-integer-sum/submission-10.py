class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = []
        for i, num in enumerate(nums):
            indexed_nums.append([num, i])
        indexed_nums.sort()

        i = 0
        j = len(indexed_nums) - 1
        
        while i < j:
            pointer = indexed_nums[i][0] + indexed_nums[j][0]
            if pointer == target:
                return [min(indexed_nums[i][1], indexed_nums[j][1]),
                max(indexed_nums[i][1], indexed_nums[j][1])]
            elif pointer < target:
                i += 1
            else:
                j -= 1
        return []