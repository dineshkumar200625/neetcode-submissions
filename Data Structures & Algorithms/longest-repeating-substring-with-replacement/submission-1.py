class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,maxlen=0,0,0
        maxfreq=0
        char={}
        while r<len(s):
            char[s[r]]=char.get(s[r],0)+1
            maxfreq=max(maxfreq,char[s[r]])
            if (r-l+1)-maxfreq>k:
                char[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen