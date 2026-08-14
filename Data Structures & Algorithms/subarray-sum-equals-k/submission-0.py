class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        freq={0:1}
        currsum=0
        for i in nums:
            currsum+=i
            if currsum-k in freq:
                count+=freq[currsum-k]
            freq[currsum]=freq.get(currsum,0)+1
        return count