class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1={}
        str2={}
        for a in s:
            str1[a]=str1.get(a,0)+1
        for b in t:
            str2[b]=str2.get(b,0)+1
        return str1 == str2