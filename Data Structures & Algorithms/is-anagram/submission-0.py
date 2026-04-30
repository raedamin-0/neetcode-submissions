class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = []
        sorted_t = []
        for i in s:
            sorted_s.append(i)
        for i in t:
            sorted_t.append(i)
        sorted_s.sort()
        sorted_t.sort()
        if sorted_s == sorted_t:
            return True
        return False
        