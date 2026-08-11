class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        h=len(nums)-1
        i=0
        while i<=h:
            if nums[i]<1:
                nums[i],nums[l]=nums[l],nums[i]
                i+=1
                l+=1
            elif nums[i]>1:
                nums[i],nums[h]=nums[h],nums[i]
                h-=1
            else:
                i+=1