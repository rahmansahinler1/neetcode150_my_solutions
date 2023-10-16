from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        
        for str in strs:
            sorted_str = sorted(str) 
            ans[tuple(sorted_str)].append(str)
        
        return ans.values()
    