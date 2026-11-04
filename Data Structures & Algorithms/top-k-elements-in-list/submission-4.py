class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = dict()
        for i in range(len(nums)):
            hash[nums[i]] = 0
        for i in range(len(nums)):
            if hash[nums[i]] == 0:
                hash[nums[i]] = 1
            else:
                hash[nums[i]] += 1
        sortedHash = dict(sorted(hash.items(), key=lambda item: item[1], reverse=True))
        mostFrequent = list(sortedHash)
        return mostFrequent[:k]