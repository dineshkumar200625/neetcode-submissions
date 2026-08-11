from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        c=0
        res=[]
        sorted_freq=sorted(count.items(), key = lambda x: x[1], reverse=True)
        for i,j in sorted_freq:
            if c==k:
                break
            res.append(i)
            c+=1
        return res