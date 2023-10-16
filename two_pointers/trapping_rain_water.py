class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        
        max_left = height[l]
        max_right = height[r]

        result = 0
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                result += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                result += max_right - height[r]
                
        return result
