'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Usage of Dictionary
Usage of dic enumerate(key,value)

#1，第二次计算从dic[s{i]]+1开始，如abdcd，从c再次开始
#2，method1是发现重复字符后，先计算ans长度，i-start;再更新start值 dic[ch]+1
#3，method2是在不重复的时候随时记录字符长度故为i-start+1
'''
class Solution:
    def lenOfLongestSubstr(self,s:str)->int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        dic ={}
        start,ans = 0,0
        for i,ch in enumerate(s) :
            if ch in dic and dic[ch] >= start:
                start +=dic[ch]+1 #新的次start从dic【s{i]]+1开始
            else:
                ans = max(ans,i-start+1)
            dic[ch] = i

        return ans

s = Solution()
s1 = ""
s2 = "a"
s3 ="bdbcb b"
s4="abcabcbb"
s5="bbbbb"
s6="pwwkew"
print(s.lenOfLongestSubstr(s1))
print(s.lenOfLongestSubstr(s2))
print(s.lenOfLongestSubstr(s3))
print(s.lenOfLongestSubstr(s4))
print(s.lenOfLongestSubstr(s5))
print(s.lenOfLongestSubstr(s6))