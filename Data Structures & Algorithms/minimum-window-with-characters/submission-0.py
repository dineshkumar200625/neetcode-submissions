class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l,r=0,0
        needed={}
        minlen=float('inf')
        for i in t:
            needed[i]=needed.get(i,0)+1
        required=len(needed)
        have={}
        formed=0
        ans_l=0
        ans_r=0
        while r<len(s):
            have[s[r]]=have.get(s[r],0)+1
            if s[r] in needed and have[s[r]]==needed[s[r]]:
                formed+=1
            while formed == required:
                if r-l+1 < minlen:
                    minlen=r-l+1
                    ans_l=l
                    ans_r=r
                left_char=s[l]
                have[left_char]-=1
                if left_char in needed and have[left_char]<needed[left_char]:
                    formed-=1
                l+=1
            r+=1
        if minlen == float("inf"):
            return ""

        return s[ans_l:ans_r + 1]
