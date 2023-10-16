class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * len(nums)
        # calculate the prefix and update result
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        # calculate the postfix and update result
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix = postfix * nums[i + 1]
            result[i] = result[i] * postfix
            
        return result
