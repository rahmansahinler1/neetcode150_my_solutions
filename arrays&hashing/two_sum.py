class Solution(object):
    def twoSum(self, nums, target):
        indexes = [] 
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    temp_indexes = [i, j]
                    temp_indexes.sort()
                    if temp_indexes not in indexes:
                        indexes.append(temp_indexes)    
        return indexes[0]
