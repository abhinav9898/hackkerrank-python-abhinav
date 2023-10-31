from ast import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occ= nums.count(val)
        k= len(nums)-occ
        i=0
        while i < k:
            if nums[i]==val:
                nums.pop(i)
                nums.append(val)
            else:
                i=i+1
        return k