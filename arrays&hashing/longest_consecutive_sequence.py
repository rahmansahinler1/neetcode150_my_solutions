class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        
        longest = 0
        for num in nums:
            # check the num is a beginning of a consecutive sequence or not
            if (num - 1) not in num_set:
                # it could be the longest sequence, so we update it's length
                length = 0
                while(num + length) in num_set:
                        length += 1
                longest = max(length, longest)
        return longest
