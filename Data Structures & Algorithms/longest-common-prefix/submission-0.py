class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=min(strs)
        mx=max(strs)
        res=""
        for i in range(len(m)):
            if m[i] != mx[i]:
                break
            res+=m[i]
        return res