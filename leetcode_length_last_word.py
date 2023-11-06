class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst= s.split()
        size= len(lst)
        end= lst[size-1]
        return len(end)