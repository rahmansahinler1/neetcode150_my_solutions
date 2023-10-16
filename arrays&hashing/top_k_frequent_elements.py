class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        occ = [[] for _ in range(len(nums) + 1)]
        result = []
        
        for number in nums:
            count[number] = 1 + count.get(number, 0)

        for number, count in count.items():
            occ[count].append(number)
        
        for count in range(len(occ) - 1, 0, -1):
            for number in occ[count]:
                result.append(number)
                if len(result) == k:
                    return result
