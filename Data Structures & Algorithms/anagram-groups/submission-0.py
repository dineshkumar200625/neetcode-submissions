class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        arr=[]
        for word in strs:
            key=tuple(sorted(word))
            groups.setdefault(key,[]).append(word)
        for j in groups.values():
            arr.append(j)
        return arr