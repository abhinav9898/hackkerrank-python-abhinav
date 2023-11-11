from ast import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res= []
        spos=-1
        lpos=-1

        for i,a in enumerate(nums):
            if a== target:
                spos= i
                res.append(spos)
                break
        if spos==-1:
            res.append(spos)
            res.append(lpos)
        else:
            for i in range(len(nums)-1, spos-1, -1):
                if nums[i]== target:
                    lpos=i
                    res.append(lpos)
                    break
        return res