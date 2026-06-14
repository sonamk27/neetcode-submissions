class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in seen:
                del seen[s[left]]
                left+=1
            seen[s[right]]=True
            if right-left+1>max_len:

                max_len = right - left + 1
        return max_len     
    

        