import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        l = 0
        h = len(nums) - 1

        self.quickSort(nums, l, h)

        return nums

    def quickSort(self, nums, l, h):

        if l >= h:
            return

        pivot = self.partition(nums, l, h)

        self.quickSort(nums, l, pivot - 1)
        self.quickSort(nums, pivot + 1, h)

    def partition(self, nums, l, h):
        pivot_index = random.randint(l, h)
        nums[pivot_index], nums[h] = nums[h], nums[pivot_index]

        pivot = nums[h]
        i = l - 1

        for j in range(l, h):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[h] = nums[h], nums[i + 1]

        return i + 1