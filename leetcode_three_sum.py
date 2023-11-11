class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        for i, a in enumerate(nums):
            if i>0 and a== nums[i-1]:
                continue
            
            l,r= i+1, len(nums)-1
            while l<r:
                threeSum= a + nums[l] + nums[r]
                if threeSum==0:
                    res.append([a, nums[l], nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
                elif threeSum < 0:
                    l=l+1
                elif threeSum > 0:
                    r=r-1
        return res