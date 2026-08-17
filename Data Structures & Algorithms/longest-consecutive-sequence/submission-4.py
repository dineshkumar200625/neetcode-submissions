class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        prev={}
        count=0
        for i in nums:
            if i-1 in prev:
                prev[i]=prev[i-1]+1
            else:
                prev[i]=1
        li=[i for i in prev.values()]
        if li != []:
            return max(li)
        return 0