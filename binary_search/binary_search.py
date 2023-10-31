"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid_index = int((r + l) / 2)
            check_value = nums[mid_index]
            if check_value < target:
                l = mid_index + 1
            elif check_value > target:
                r = mid_index - 1
            else:
                return mid_index
        return -1
            
            
nums = [-1,0,3,5,9,12]
target = 9

nums1 = [-1,0,3,5,9,12]
target1 = 2

nums2 = [2, 5]
target2 = 2

sol = Solution()

print(sol.search(nums, target))
print(sol.search(nums1, target1))
print(sol.search(nums2, target2))
