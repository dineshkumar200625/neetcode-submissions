from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        n=len(nums)
        res=[]
        for i,j in count.items():
            if j > n//3:
                res.append(i)
        return res