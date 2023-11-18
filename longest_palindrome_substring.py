class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxTemp=s[0]
        maxCount=1
        temp=s[0]
        if len(s)==1 or s==s[::-1]:
            return s
        else:
            for l in range(0, len(s)-1//2):
                temp=s[l]
                r=l+1
                count=1
                while r<len(s):
                    temp+=s[r]
                    count+=1
                    if s[l]==s[r] and s[l:r+1]==temp[::-1] and count>maxCount:
                        maxTemp= temp
                        maxCount= count
                    r+=1
            return maxTemp