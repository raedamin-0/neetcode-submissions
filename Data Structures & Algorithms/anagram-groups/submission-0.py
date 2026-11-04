class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = dict()
        for i in range(len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            if sortedStr not in hash:
                hash[sortedStr] = []
            hash[sortedStr].append(strs[i])
        return list(hash.values())                