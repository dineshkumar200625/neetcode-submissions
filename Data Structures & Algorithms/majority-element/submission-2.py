from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=Counter(nums)
        for i,j in k.items():
            if j> len(nums)/2:
                return i
        return -1