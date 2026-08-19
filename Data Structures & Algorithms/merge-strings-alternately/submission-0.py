class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        n=min(len(word1),len(word2))
        s=""
        while left<n:
            s+=word1[left]
            s+=word2[left]
            left+=1
        if len(word1)==n:
            s+=word2[left:]
        else:
            s+=word1[left:]
        return s