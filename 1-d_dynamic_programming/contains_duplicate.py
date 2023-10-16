import numpy as np

class Solution(object):
    def containsDuplicate(self, nums):
        arr = np.array(nums)
        
        if arr.size != np.unique(arr).size:
            return True
        else:
            return False