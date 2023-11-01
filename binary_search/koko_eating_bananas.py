"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas 
and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""
import numpy as np
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # check start will start from np.ceil(sum(piles) / h).
        l, r = 0, max(piles)
        check = int(np.ceil(sum(piles) / h))
        result = max(piles)
        
        while l <= r and check:
            num_of_step = 0
            for num_of_banana in piles:               
                num_of_step += np.ceil(num_of_banana / check)  
            if num_of_step > h:
                l = check + 1   
            elif num_of_step <= h:
                result = min(result, check)
                r = check - 1
            check = int(np.ceil((l + r) / 2))

        return result
            
            
piles = [3,6,7,11]
h = 8

piles1 = [30,11,23,4,20]
h1 = 5

piles2 = [30,11,23,4,20]
h2 = 6

piles3 = [312884470]
h3 = 312884469

piles4 = [312884470]
h4 = 968709470

sol = Solution()

print(sol.minEatingSpeed(piles, h))
print(sol.minEatingSpeed(piles1, h1))
print(sol.minEatingSpeed(piles2, h2))
print(sol.minEatingSpeed(piles3, h3))
print(sol.minEatingSpeed(piles4, h4))
