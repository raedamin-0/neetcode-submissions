class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.append("edge")
        joined_str = '\t'.join(strs)
        return joined_str

    def decode(self, s: str) -> List[str]:
        org_list = []
        stringbuilder = []
        for char in s:
            if s == '' or "":
                org_list.append("")
                return org_list
            if char == '\t':
                org_list.append(''.join(stringbuilder))
                stringbuilder = []
            else:
                stringbuilder.append(char)
        return org_list
