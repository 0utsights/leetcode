#Remove Duplicates From Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            # r loop starts sorting through the list starting at 1 and continuing throughout each number
            if nums[r] != nums[r - 1]:
                # if the current number r is on isn't equal to the previous one
                nums[l] = nums[r]
                # write the current number at position l
                l += 1
                # move l a position forward for a new number
        return l