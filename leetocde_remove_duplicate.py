from ast import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        j=0
        while i<len(nums):
            if nums[i]>nums[j]:
                i=i+1
                j=j+1
            else:
                nums.pop(i)
        return len(nums)