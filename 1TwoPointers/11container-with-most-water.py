'''
题目链接：https://leetcode.com/problems/container-with-most-water/
'''
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height)==0:
            return 0
        ans = 0
        l, r = 0,len(height)-1
        while l < r:
            ans = max(ans,min(height[l],height[r]) * (r - l))
            if height[l] >= height[r]:
                r-=1
            else:
                l+=1
        return ans

s=Solution()
height =[1,8,6,2,5,4,8,3,7]
height =[1,1]
print(s.maxArea(height))