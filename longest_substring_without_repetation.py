class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount=1
        count=1
        if s is not '':
            for i in range(0, len(s)-1):
                temp=s[i]
                maxCount= max(maxCount, count)
                count=1
                for j in range(i+1,len(s)):
                    if s[j] not in temp:
                        temp+=s[j]
                        count+=1
                    else:
                        break
            return max(maxCount, count)
        else:
            return 0