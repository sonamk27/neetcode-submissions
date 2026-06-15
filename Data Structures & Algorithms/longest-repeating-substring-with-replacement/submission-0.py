class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_freq=0
        ans=0
        for right in range(len(s)):
            ch=s[right]
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
            if count[ch]>max_freq:
                max_freq=count[ch]
            while (right-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            window=right-left+1
            if window>ans:
                ans=window
        return ans
                                
        