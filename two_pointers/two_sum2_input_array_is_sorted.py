class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            diff = numbers[r] + numbers[l]
            
            if diff > target:
                r -= 1
            elif diff < target:
                l += 1
            else:
                return [l + 1, r + 1]
