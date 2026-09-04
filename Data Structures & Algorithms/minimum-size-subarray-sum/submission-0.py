class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,su,maxlen=0,0,0,100001
        while r<len(nums):
            su+=nums[r]
            while su>=target:
                su-=nums[l]
                
            
                maxlen=min(maxlen,r-l+1)
                l+=1
            r+=1
            
        if maxlen==100001:
            return 0
        else:
            return maxlen