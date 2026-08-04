class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        res=[]
        for i,j in enumerate(nums):
            index[j]=i
        for i in range(len(nums)):
            if target-nums[i] in index and i != index[target-nums[i]]:
                res.append(index[target-nums[i]])
                res.append(i)
                break
        res.sort()
        return res