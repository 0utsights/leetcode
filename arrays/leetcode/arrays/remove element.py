class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #int k value to keep track of position
        k = 0
        #loop through the entire list
        for i in range(len(nums)):
            #if i isnt equal to the value
            if nums[i] != val:
                #set nums at position i  to nums at index position k
                nums[k] = nums[i]
                #increment k by 1 (to keep track of new length)
                k += 1
        return k 