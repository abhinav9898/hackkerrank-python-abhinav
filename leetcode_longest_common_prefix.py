class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res= ''
        for i in range(len(strs[0])):
            for ele in strs:
                if strs[0][i] != ele[i] or i==len(ele):
                    return res
            res+= strs[0][i]
        return res