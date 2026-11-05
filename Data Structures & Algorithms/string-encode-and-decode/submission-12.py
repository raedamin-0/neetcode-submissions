class Solution:

    def encode(self, strs: List[str]) -> str:
        stringbuilder = []
        for s in strs:
            stringbuilder.append(str(len(s)))
            stringbuilder.append('|')
            stringbuilder.append(s)
        return ''.join(stringbuilder)

    def decode(self, s: str) -> List[str]:
        listbuilder = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '|':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            listbuilder.append(s[i:j])
            i = j
    
        return listbuilder