"""
Given a string s, find the length of the longest 
substring
without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            l, r = 0, 1
            result = 0
            while l < len(s):
                substring = s[l]
                while r < len(s) and s[r] not in substring:
                    substring += s[r]
                    r += 1
                l += 1
                r = l + 1
                result = max(result, len(substring))   
            return result
        return 0            

s = "dvdf"
s1 = "bbbbb"
s2 = "pwwkew"

sol = Solution()

print(sol.lengthOfLongestSubstring(s))
print(sol.lengthOfLongestSubstring(s1))
print(sol.lengthOfLongestSubstring(s2))
