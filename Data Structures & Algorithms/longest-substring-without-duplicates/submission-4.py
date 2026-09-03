class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        n=len(s)
        mapp={}
        maxlen=0
        while r<n:
            if s[r]  in mapp:
                if mapp[s[r]]>=l:
                    l=mapp[s[r]]+1
            
            maxlen=max(maxlen,r-l+1)
            mapp[s[r]]=r  
            r+=1
        return maxlen