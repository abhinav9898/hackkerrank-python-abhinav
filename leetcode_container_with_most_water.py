class Solution:
    def maxArea(self, height: List[int]) -> int:
        size= len(height)
        i= 0
        j= size-1
        tempArea=0
        maxArea= 0
        while i<j:
            tempArea= (j-i)* min(height[i], height[j])
            maxArea= max(maxArea, tempArea)
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return maxArea