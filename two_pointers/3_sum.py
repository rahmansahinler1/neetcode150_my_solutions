class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if (r == i):
                    r -= 1
                    continue
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    sorted_nums = sorted([nums[i] , nums[l] , nums[r]])
                    if sorted_nums not in results:
                        results.append(sorted_nums)
                    l += 1
     
        return results
