class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0

        while l < r:
            distance = r - l
            area = min(height[l], height[r]) * distance
            result = max(result, area)
            
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return result
